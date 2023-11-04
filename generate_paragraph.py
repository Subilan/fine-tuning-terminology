from fn import dumpLine, buildLine
from os import remove

lines = open("translations/literature.txt", mode='r').readlines()

try:
    remove("paragraphs.jsonl")
except:
    pass

with open("paragraphs.jsonl", mode='a+') as paragraphs:
    for i in range(len(lines)):
        if i % 2 == 0:
            paragraphs.write(
                dumpLine(
                    buildLine(
                        f'Now I will give you a paragraph of psychological literature. Please give me the best and accurate translation in Chinese: {lines[i]:s}',
                        lines[i+1]
                    )
                )
            )
