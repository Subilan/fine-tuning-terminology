import os
import openai
from sys import argv

assert len(argv) >= 1

def main():
    if len(argv) == 1:
        print("Usage: python train.py <command> [arguments]")
        return

    cmd = argv[1]

    if cmd == "upload":
        filename = "data.jsonl" if len(argv) < 3 else argv[2]
        openai.api_key = os.getenv("OPENAI_API_KEY")
        print(openai.File.create(
            file=open("data.jsonl", "rb"),
            purpose="fine-tune"
        ))
        
    if cmd == "create":
        if len(argv) < 3:
            print("Missing required argument: file identifier")
            return
        filename = argv[2]
        model = "gpt-3.5-turbo" if len(argv) < 4 else argv[3]
        print(openai.FineTuningJob.create(training_file=filename, model=model))
        
    if cmd == "list":
        limit = 10 if len(argv) < 3 else int(argv[2])
        print(openai.FineTuningJob.list(limit=limit))

    if cmd == "retrieve" or cmd == "cancel" or cmd == "list-events":
        if len(argv) < 3:
            print("Missing required argument: job identifier")
            return
        
        job = argv[2]
        
        if cmd == "retrieve": print(openai.FineTuningJob.retrieve(job))
        if cmd == "cancel": print(openai.FineTuningJob.cancel(job))
        if cmd == "list-events":
            limit = 10 if len(argv) < 4 else argv[3]
            print(openai.FineTuningJob.list_events(id=job, limit=limit))
            
main()