import docx
import os
import re
import json

result = []

def getLanguage(text):
    if (text == None):
        return 'none'
    return 'zh' if re.findall(r'[\u4e00-\u9fff]+', text) else 'en'


collection = []
collectionCursor = -1

entries = [x for x in os.scandir('origin/docx')]

for e in range(len(entries)):
    entry = entries[e]
    paragraphs = docx.Document(f'origin/docx/{entry.name:s}').paragraphs
    currentLanguage = None
    for i in range(len(paragraphs)):
        currentParagraph = paragraphs[i].text
        if len(currentParagraph.strip()) == 0 or currentParagraph == '\n':
            continue

        # if re.findall(r'[\u4e00-\u9fff]+', currentParagraph):
        #     if re.findall(r'[A-Za-z]{3,}', currentParagraph):
        #         if not re.findall(r'\d+', currentParagraph):
        #             print(entry)
        #             print(currentParagraph)
        #             print('---')

        if getLanguage(currentParagraph) != currentLanguage:
            collection.append([currentParagraph])
            collectionCursor += 1
            currentLanguage = getLanguage(currentParagraph)
        elif getLanguage(currentParagraph) == currentLanguage:
            collection[collectionCursor].append(currentParagraph)

for i in range(len(collection)):
    if i % 2 == 0:
        result.append({'en': ' '.join(collection[i]), 'zh': ' '.join(collection[i+1])})
try:
    os.remove('origin/pairs.json')
except:
    pass
json.dump(result, open('origin/pairs.json', mode='w'), ensure_ascii=False)
