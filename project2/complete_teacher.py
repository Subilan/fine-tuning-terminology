import json
import argparse
import subprocess
from models import latest_teacher_model

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--model')
parser.add_argument('question')
args = parser.parse_args()
    
subprocess.run(f'python3 ./complete.py "{args.question:s}" --model {latest_teacher_model if args.model == None else args.model:s}', shell=True, encoding='utf-8')