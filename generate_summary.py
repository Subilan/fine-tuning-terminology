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

index = 1
# with open("summary/summary_{0}.csv".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")), encoding='utf-8-sig', mode='w+') as summary:
for original in to_translate:
    print(f"row: {index:d}")
    input_question = default_prompt_template.format(original.replace('\n', ''))
    command = "python3 ./translate.py {0} -m {1}".format(quote(input_question), latest_job['fine_tuned_model'])
    print("> {0}".format(command))
    result = run(command, shell=True, stdout=PIPE)
    result_rows.append([
        input_question,
        result.stdout.decode(),
        dumpSimple(buildPrompt("<>")),
        latest_job['id'],
        latest_job['trained_tokens'],
        f'${0.008 * float(latest_job["trained_tokens"]) / 1000:f}',
        latest_job['fine_tuned_model']
    ])
    index += 1

pandas.DataFrame(result_rows, columns=['请求文本', '返回结果', 'Prompt模板', 'Job ID', '训练消耗Token', '预估花费', '模型名称']).to_excel("summary/summary_{0}.xlsx".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")))
