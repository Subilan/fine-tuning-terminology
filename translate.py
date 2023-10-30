from argparse import ArgumentParser
from generate_summary import default_system_message
import openai

parser = ArgumentParser(prog='get-translation')
parser.add_argument('prompt')
parser.add_argument('-m', '--model')
parser.add_argument('-s', '--system')

args = parser.parse_args()

prompt = args.prompt
model = args.model
system_content = args.system if args.system != None else default_system_message

if prompt == None:
    print('No prompt!')
elif model == None:
    print('No model!')
else:
    result = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content or ""},
            {"role": "user", "content": prompt or ""}
        ]
    )
    
    print(result.choices[0].message.content.replace(' END', ''))
