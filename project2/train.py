from apikey import OPENAI_API_KEY
import openai
import argparse
import datetime
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-m', '--model')
parser.add_argument('-n', '--nepochs')
parser.add_argument('-t', '--target')
args = parser.parse_args()

openai.api_key = OPENAI_API_KEY

if args.file == None or args.model == None:
    print('missing required arguments')
    exit()

result = openai.FineTuningJob.create(
    training_file=args.file,
    model=args.model,
    suffix=args.target,
    hyperparameters={'n_epochs': int(args.nepochs) if args.nepochs != None else 3}
)

print(f'created: ({args.target:s}) <{result.object:s}> {result.id:s} based on {result.model:s} at {datetime.datetime.fromtimestamp(result.created_at).strftime("%Y/%m/%d %H:%M:%S"):s}')

while 1:
    retrieved = openai.FineTuningJob.retrieve(result.id)
    print(f'[{datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"):s}] {retrieved.status:s}')
    if retrieved.status == 'succeeded':
        print(f'{args.target:s} training complete: model={result.model:s}, fine_tuned_model={retrieved.fine_tuned_model:s}, trained_tokens={retrieved.trained_tokens:d}, estimated_cost=${retrieved.trained_tokens / 1000 * 0.008:.2f}')
        break
    sleep(1.0)