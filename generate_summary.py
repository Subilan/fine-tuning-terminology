import openai
import os
import datetime
import pandas
from subprocess import run, PIPE
from fn import default_prompt_template, default_system_message, dumpSimple, buildPrompt
from json import dumps
from shlex import quote

openai.api_key = os.getenv("OPENAI_API_KEY")

latest_job = openai.FineTuningJob.list(limit=1).data[0]

to_translate = open("to_translate.txt", mode='r').readlines()

result_rows = []

repetition_count = 10

result_pairs_header = ['原文']
result_pairs_header.extend(['返回结果#{0}'.format(i + 1) for i in range(repetition_count)])

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
        result_row.extend(result.stdout.decode())
    result_rows.append(result_row)
    index += 1

with pandas.ExcelWriter(f"summary/summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'):s}.xlsx") as writer:
    pandas.DataFrame(result_rows).to_excel(writer, sheet_name='ResultPairs', index=False, header=result_pairs_header)
    pandas.DataFrame([
        [
            dumpSimple(buildPrompt(default_prompt_template.format("<原文>"))),
            latest_job['id'],
            latest_job['trained_tokens'],
            f'${0.008 * float(latest_job["trained_tokens"]) / 1000:f}',
            latest_job['fine_tuned_model']
        ]
    ]).to_excel(writer, sheet_name='Properties', index=False, header=['Prompt模板', 'Job ID', '消耗Token', '预估花费', '模型名称'])
