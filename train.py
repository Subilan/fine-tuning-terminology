import os
import openai
from sys import argv
from argparse import ArgumentParser
from apikey import OPENAI_API_KEY

parser = ArgumentParser(
    prog="train",
    description="Provide commands that call corresponding OpenAI API with customizable arguments.",
)

parser.add_argument("command")
parser.add_argument('-i', '--identifier')
parser.add_argument('-l', '--limit')
parser.add_argument('-f', '--filename')
parser.add_argument('-m', '--model')
parser.add_argument('-cu', '--contentUser')
parser.add_argument('-cs', '--contentSystem')
args = parser.parse_args()

openai.api_key = OPENAI_API_KEY

def main():
    match (args.command):
        case "upload":
            filename = args.filename
            if filename == None:
                print("Missing required argument 'filename'.")
                return
            print(openai.File.create(
                file=open(filename, "rb"),
                purpose="fine-tune"
            ))

        case "create":
            fileid = args.identifier
            model = args.model
            if fileid == None:
                print("Missing required argument 'identifier'.")
                return
            if model == None:
                print("Missing required argument 'model'.")
                return
            print(openai.FineTuningJob.create(training_file=fileid, model=model))
            
        case "list":
            limit = int(args.limit) if args.limit != None else None
            if limit == None:
                print("Missing optional argument 'limit', default to 10.")
                limit = 10
            print(openai.FineTuningJob.list(limit=limit))
            
        case "retrieve" | "cancel" | "list-events":
            jobid = args.identifier
            limit = int(args.limit) if args.limit != None else None
            if jobid == None:
                print("Missing required argument 'identifier'.")
                return
            match args.command:
                case "retrieve":
                    print(openai.FineTuningJob.retrieve(jobid))
                
                case "cancel":
                    print(openai.FineTuningJob.cancel(jobid))
                    
                case "list-events":
                    if limit == None:
                        print("Missing optional argument 'limit', default to 10.")
                        limit = 10
                    print(openai.FineTuningJob.list_events(id=jobid, limit=limit))

        case "create-completion":
            model = args.model
            user_content = args.contentUser
            system_content = args.contentSystem
            completion = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_content or ""},
                    {"role": "user", "content": user_content or ""}
                ]
            )
            print(completion)

        case _:
            parser.print_help()
main()