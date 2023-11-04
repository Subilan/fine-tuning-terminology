import openai
import os
import datetime
import pandas
from subprocess import run, PIPE
from fn import default_prompt_template, default_system_message, dumpSimple, buildPrompt
from json import dumps
from shlex import quote
from csv import DictReader

openai.api_key = os.getenv("OPENAI_API_KEY")

latest_job = openai.FineTuningJob.list(limit=1).data[0]

if latest_job.status != 'succeeded':
    print("Fine-tuning job is not completed.")
    exit()

to_translate = open("to_translate.txt", mode='r').readlines()

result_rows = []

repetition_count = 10

result_pairs_header = ['原文']
result_pairs_header.extend(['返回结果#{0}'.format(i + 1) for i in range(repetition_count)])
result_pairs_header.append('稳定性')

target_terms = []

with open('terminology.csv', mode='r') as terms:
    reader = DictReader(terms)
    collection = [row for row in reader]
    index = 0
    for originalText in to_translate:
        target_terms.append([])
        for row in collection:
            if row['English'].lower() in originalText.lower():
                if not row['Chinese'] in target_terms[index]: target_terms[index].append(row['Chinese']) # Distinct
        index += 1
        
index = 1
# with open("summary/summary_{0}.csv".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")), encoding='utf-8-sig', mode='w+') as summary:
for originalText in to_translate:
    print(f"Compiling row {index:d}")
    input_question = default_prompt_template.format(originalText.replace('\n', ''))
    result_row = [originalText]
    for i in range(repetition_count):
        print(f"Building translation#{i+1:d}")
        command = "python3 ./translate.py {0} -m {1}".format(quote(input_question), latest_job['fine_tuned_model'])
        result = run(command, shell=True, stdout=PIPE)
        result_row.append(result.stdout.decode())
    
    current_target_terms = target_terms[index - 1]
    
    print(current_target_terms)
    
    satisfied_term_dict = dict()
    for t in current_target_terms: satisfied_term_dict[t] = 0 # Initialize terms counter field for current sentence.
    for i in range(repetition_count): # For every version of translation
        current_translation_version = result_row[i + 1] # Get the current version of translation
        for t in current_target_terms: # For every terminology that needs to be satisfied
            if t in current_translation_version: # If satisfied
                # Note: this must be done before printing out.
                satisfied_term_dict[t] += 1 # Increment corresponding value in satisifed_term_dict
                print(f"Satified: {t:s}; Total: {satisfied_term_dict[t]:d}/{repetition_count:d}")
                
                
    stability_description = ""
    for t in current_target_terms:
        stability_description += f'{t:s}={satisfied_term_dict[t]/repetition_count*100:.2f}%;'
    result_row.append(stability_description if stability_description != "" else "没有术语")
    result_rows.append(result_row)
    index += 1

with pandas.ExcelWriter(f"summary/summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'):s}.xlsx") as writer:
    pandas.DataFrame(result_rows).to_excel(writer, sheet_name='ResultPairs', header=result_pairs_header)
    pandas.DataFrame([
        [
            dumpSimple(buildPrompt(default_prompt_template.format("<原文>"))),
            latest_job['id'],
            latest_job['trained_tokens'],
            f'${0.008 * float(latest_job["trained_tokens"]) / 1000:f}',
            latest_job['fine_tuned_model']
        ]
    ]).to_excel(writer, sheet_name='Properties', header=['Prompt模板', 'Job ID', '消耗Token', '预估花费', '模型名称'])
