from argparse import ArgumentParser

parser = ArgumentParser(prog='join.py')
parser.add_argument("filenames", nargs='*')
parser.add_argument('-o', '--output')

args = parser.parse_args()
if args.filenames == None:
    exit()

filenames = args.filenames
outputfile = 'output.jsonl' if args.output == None else args.output

result = []
for f in filenames:
    result.extend(open(f).readlines())

with open(outputfile, mode='w+') as opt:
    opt.writelines(result)