from apikey import OPENAI_API_KEY
import openai
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('question')
parser.add_argument('-m', '--model')
args = parser.parse_args()

openai.api_key = OPENAI_API_KEY

result = openai.ChatCompletion.create(
    model=args.model,
    messages=[
        {
            'role': 'system',
            'content': 'You are a translator who can translate Chinese to English, and English to Chinese.' if args.model == 'translator' else 'You are a teacher model that would give assessment on translation generated by other model, and also giving the reason and a better translation.'
        },
        {
            'role': 'user',
            'content': args.question
        }
    ]
)

print(result.choices[0].message.content)