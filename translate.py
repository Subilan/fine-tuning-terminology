from argparse import ArgumentParser
import openai

parser = ArgumentParser(prog='get-translation')
parser.add_argument('prompt')
parser.add_argument('-m', '--model')
parser.add_argument('-s', '--system')

args = parser.parse_args()

prompt = args.prompt
model = args.model
system_content = 'You are a psychologist chatbot that can accurately translate the terminologies in literature in his area to Chinese.'

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
