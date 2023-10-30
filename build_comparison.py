from os import remove
import csv
from fn import dumps, withRoles
import random

possible_questions = [
    "Original text: '{0}' please improve the translation '{1}' to fit Chinese language rules.",
    "Original text is '{0}', what is the better version of '{1}'?",
    "Given the original text '{0}, the translation '{1}' can be improved. Please give me the desired output."
]

try:
    remove("comparison.jsonl")
except:
    pass

with open("comparison.jsonl", mode='a') as comparisonData:
    with open("comparison_002.csv", mode='r', encoding="utf-8-sig") as comparisons:
        reader = csv.DictReader(comparisons)
        for row in reader:
            comparisonData.write(dumps({
                'messages': withRoles(
                    question=possible_questions[random.randint(0, len(possible_questions) - 1)].format(row['OriginalContent'], row['BadTranslation']),
                    answer=row["GoodTranslation"]
                )
            }))
            comparisonData.write("\n")
