import re
import nltk
from fn import withRoles, toJsonl, removeReturn
from os import remove

with open("translations/literature.txt", mode='r+') as literature:
    lines = literature.readlines()
    withoutReturn = [line for line in lines if line != '\n']
    separated = []
    index = 0
    for line in withoutReturn:
        parts = []
        # if (index % 2 == 0): parts = nltk.tokenize.sent_tokenize(line) re.findall("\w{3,}\.", line)
        # Note: NLTK cannot process abbrs. such as pp. well.
        if (index % 2 == 0):
            parts = re.split(re.compile("\w{3,}）?\.\s"), line)
            i = 0
            for word in re.findall("\w{3,}）?\.\s", line):
                 parts[i] += word
                 i += 1
        else:
            parts = line.split("。")
        separated.append(parts)
        index += 1
        
    try:
        remove("literature.jsonl")
    except:
        pass
    
    with open("literature.jsonl", mode='a') as separated_literature:
        index = 0
        for s in separated:
            if index < len(separated):
                currentTargetEnglish = separated[index]
                currentTargetChinese = separated[index + 1]
                for i in range(len(currentTargetEnglish) - 1): # minus 1 to adapt array index expression (0~len-1)
                    # separated_literature.write(currentTargetEnglish[i])
                    # separated_literature.write(currentTargetChinese[i])
                    separated_literature.write(toJsonl(withRoles(
                        "Please translate the psychology literature paragraph '{0}' into Chinese accurately.".format(removeReturn(currentTargetEnglish[i])),
                        removeReturn(currentTargetChinese[i])
                    )))
            index += 2