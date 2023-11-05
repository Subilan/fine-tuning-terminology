from apikey import OPENAI_API_KEY
import openai
import argparse
import datetime
from time import sleep
import json

from models import latest_teacher_model, latest_translator_model

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-n', '--nepochs')
parser.add_argument('-t', '--target')
parser.add_argument('-m', '--model')
args = parser.parse_args()

openai.api_key = OPENAI_API_KEY

if args.file == None or args.target == None:
    print('missing required arguments')
    exit()
    
if args.target != 'teacher' and args.target != 'translator':
    print('invalid training target')
    exit()

target_model = latest_teacher_model if args.target == 'teacher' else latest_translator_model

if args.model != None:
    target_model = args.model

result = openai.FineTuningJob.create(
    training_file=args.file,
    model=target_model,
    suffix=args.target,
    hyperparameters={'n_epochs': int(args.nepochs) if args.nepochs != None else 'auto'}
)

try:
    print(f'created: ({args.target:s}) <{result.object:s}> {result.id:s} based on {result.model:s} at {datetime.datetime.fromtimestamp(result.created_at).strftime("%Y/%m/%d %H:%M:%S"):s}')
except:
    print('Unable to format creation message. Crucial information is as follows.')
    print('args.target=' + args.target)
    print('result.id=' + result.id)
    print('result.model=' + result.model)

while 1:
    retrieved = openai.FineTuningJob.retrieve(result.id)
    print(f'[{datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"):s}] {retrieved.status:s}')
    if retrieved.status == 'succeeded':
        with open('fine_tuned_models.json', 'r+', encoding='utf-8') as ft_models:
            data = json.load(ft_models)
            data[args.target].append(retrieved)
            ft_models.truncate(0)
            ft_models.write(json.dumps(data))
        print(f'{args.target:s} training complete: model={result.model:s}, fine_tuned_model={retrieved.fine_tuned_model:s}, trained_tokens={retrieved.trained_tokens:d}, estimated_cost=${retrieved.trained_tokens / 1000 * 0.008:.2f}')
        break
    sleep(1.0)