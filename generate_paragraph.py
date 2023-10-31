from fn import dumpLine, buildLine

lines = open("translations/literature.txt", mode='r').readlines()

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
