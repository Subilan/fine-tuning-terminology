import json
import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('question')
args = parser.parse_args()

latest_teacher_model = ''

with open("fine_tuned_models.json", mode='r') as ft:
    data = json.load(ft)
    latest_teacher_model = [x['fine_tuned_model'] for x in data['teacher']][0]
    
subprocess.run(f'python3 ./complete.py "{args.question:s}" --model {latest_teacher_model:s}', shell=True, encoding='utf-8')