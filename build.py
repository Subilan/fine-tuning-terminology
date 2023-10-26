import csv
from random import randint
from json import dumps
from os import remove

possible_questions = [
    "What is the translation of the psychological term {0} in Chinese?",
    "Can you provide the Chinese translation for the psychological term {0}?",
    "How is the psychological term {0} translated into Chinese?",
    "Please translate the psychological term {0} into Chinese.",
    "I would like to know how to say the psychological term {0} in Chinese.",
    "What is the equivalent of the psychological term {0} in Chinese?",
    "Could you please provide the Chinese translation for the psychological term {0}?",
    "What is the Chinese term for the psychological concept {0}?",
    "How would you express the psychological term {0} in Chinese?",
    "Can you help me with the Chinese translation of the psychological term {0}?",
    "What is the Chinese counterpart of the psychological term {0}?",
    "Please tell me how to translate the psychological term {0} into Chinese.",
    "What is the Chinese rendition of the psychological term {0}?",
    "How do they say the psychological term {0} in Chinese?",
    "Could you give me the Chinese translation for the psychological term {0}?",
    "What would be the Chinese rendering of the psychological term {0}?",
    "Please provide the Chinese equivalent for the psychological term {0}.",
    "How should I translate the psychological term {0} into Chinese?",
    "Can you explain the Chinese translation of the psychological term {0}?",
    "What do they call the psychological term {0} in Chinese?",
    "What is the Chinese version of the psychological term {0}?",
    "Please give me the Chinese term for the psychological term {0}.",
    "How is the psychological term {0} commonly translated into Chinese?",
    "What is the accepted Chinese translation for the psychological term {0}?",
    "Can you suggest the Chinese translation of the psychological term {0}?",
    "What would be the appropriate Chinese translation for the psychological term {0}?",
    "Please clarify the Chinese translation of the psychological term {0}.",
    "How do I express the psychological term {0} in Chinese?",
    "What is the proper Chinese translation of the psychological term {0}?",
    "Could you provide the Chinese rendering for the psychological term {0}?",
    "How do Chinese speakers refer to the psychological term {0}?",
    "Please suggest the Chinese equivalent of the psychological term {0}.",
    "What is the standard Chinese translation for the psychological term {0}?",
    "How do you say the psychological term {0} in Mandarin Chinese?",
    "What is the commonly used Chinese translation for the psychological term {0}?",
    "Could you help me with the Chinese translation of the psychological term {0}?",
    "What is the correct Chinese translation of the psychological term {0}?",
    "How should I convey the psychological term {0} in Chinese?",
    "Please share the Chinese term for the psychological term {0}.",
    "What is the most accurate Chinese translation for the psychological term {0}?",
    "How is the psychological term {0} typically translated in Chinese?",
    "What is the native Chinese term for the psychological term {0}?",
    "Can you translate the psychological term {0} into Chinese for me?",
    "What is the best way to translate the psychological term {0} into Chinese?",
    "Please provide the Chinese translation for the psychological term {0}.",
    "What is the Chinese word that represents the psychological term {0}?",
    "How would the psychological term {0} be translated into Chinese?",
    "What is the appropriate Chinese translation for the psychological term {0}?",
    "Can you help me find the Chinese translation for the psychological term {0}?",
    "What do you call the psychological term {0} in Chinese?",
    "What is the Chinese translation equivalent for the psychological term {0}?",
]


def based(question, answer):
    return [
        {"role": "system", "content": "Linga is a psychologist chatbot that can accurately translate the terminologies in literature in his area to Chinese."},
        {"role": "user", "content": question},
        {"role": "assistant", "content": answer}
    ]

remove("data.jsonl")

with open("data.jsonl", mode="a", encoding="utf-8") as file:
    with open("terminology.csv", newline='') as translations:
        reader = csv.DictReader(translations)
        for row in reader:
            result = based(
                possible_questions[randint(0, len(possible_questions) - 1)].format(row["English"].lower()) + "\n\nTranslation:\n\n",
                row["Chinese"] + " END"
            )
            file.write(dumps({"messages": result}, ensure_ascii=False) + "\n")
