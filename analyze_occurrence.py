from subprocess import run, PIPE
from argparse import ArgumentParser
from time import perf_counter

parser = ArgumentParser(prog='analyze_occurrence.py')
parser.add_argument('text')
parser.add_argument('-m', '--model')
parser.add_argument('-t', '--target')
parser.add_argument('-r', '--repetition')
parser.add_argument('-e', '--expect')

args = parser.parse_args()

repetition_count = int(args.repetition) if args.repetition != None else 1
expectation_count = int(args.expect) if args.expect != None else 1
occurrence = 0

time_total = 0.0

for i in range(repetition_count):
    t1 = perf_counter()
    print("Call index #{0}".format(i))
    result = run('python3 ./translate.py "{0}" -m {1}'.format(args.text, args.model), shell=True, stdout=PIPE)
    result_string = result.stdout.decode()
    t2 = perf_counter()
    print("Time elapsed {0}s".format(t2-t1))
    if result_string.count(args.target) >= expectation_count:
        occurrence += 1
        print("-> pass")
    else:
        print("-> miss")
    time_total += t2 - t1
    
print(f"occurrence={occurrence:d}, time_elapsed:{time_total:.3f}")