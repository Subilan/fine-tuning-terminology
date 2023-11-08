import csv
import json
import random
import os

system_message = 'You are a translator who can translate Chinese to English, and English to Chinese.'

possible_questions = [
    "What is the translation of the psychological term '{0}' in Chinese?",
    "Can you provide the Chinese translation for the psychological term '{0}'?",
    "How is the psychological term '{0}' translated into Chinese?",
    "Please translate the psychological term '{0}' into Chinese.",
    "I would like to know how to say the psychological term '{0}' in Chinese.",
    "What is the equivalent of the psychological term '{0}' in Chinese?",
    "Could you please provide the Chinese translation for the psychological term '{0}'?",
    "What is the Chinese term for the psychological concept '{0}'?",
    "How would you express the psychological term '{0}' in Chinese?",
    "Can you help me with the Chinese translation of the psychological term '{0}'?",
    "What is the Chinese counterpart of the psychological term '{0}'?",
    "Please tell me how to translate the psychological term '{0}' into Chinese.",
    "What is the Chinese rendition of the psychological term '{0}'?",
    "How do they say the psychological term '{0}' in Chinese?",
    "Could you give me the Chinese translation for the psychological term '{0}'?",
    "What would be the Chinese rendering of the psychological term '{0}'?",
    "Please provide the Chinese equivalent for the psychological term '{0}'.",
    "How should I translate the psychological term '{0}' into Chinese?",
    "Can you explain the Chinese translation of the psychological term '{0}'?",
    "What do they call the psychological term '{0}' in Chinese?",
    "What is the Chinese version of the psychological term '{0}'?",
    "Please give me the Chinese term for the psychological term '{0}'.",
    "How is the psychological term '{0}' commonly translated into Chinese?",
    "What is the accepted Chinese translation for the psychological term '{0}'?",
    "Can you suggest the Chinese translation of the psychological term '{0}'?",
    "What would be the appropriate Chinese translation for the psychological term '{0}'?",
    "Please clarify the Chinese translation of the psychological term '{0}'.",
    "How do I express the psychological term '{0}' in Chinese?",
    "What is the proper Chinese translation of the psychological term '{0}'?",
    "Could you provide the Chinese rendering for the psychological term '{0}'?",
    "How do Chinese speakers refer to the psychological term '{0}'?",
    "Please suggest the Chinese equivalent of the psychological term '{0}'.",
    "What is the standard Chinese translation for the psychological term '{0}'?",
    "How do you say the psychological term '{0}' in Mandarin Chinese?",
    "What is the commonly used Chinese translation for the psychological term '{0}'?",
    "Could you help me with the Chinese translation of the psychological term '{0}'?",
    "What is the correct Chinese translation of the psychological term '{0}'?",
    "How should I convey the psychological term '{0}' in Chinese?",
    "Please share the Chinese term for the psychological term '{0}'.",
    "What is the most accurate Chinese translation for the psychological term '{0}'?",
    "How is the psychological term '{0}' typically translated in Chinese?",
    "What is the native Chinese term for the psychological term '{0}'?",
    "Can you translate the psychological term '{0}' into Chinese for me?",
    "What is the best way to translate the psychological term '{0}' into Chinese?",
    "Please provide the Chinese translation for the psychological term '{0}'.",
    "What is the Chinese word that represents the psychological term '{0}'?",
    "How would the psychological term '{0}' be translated into Chinese?",
    "What is the appropriate Chinese translation for the psychological term '{0}'?",
    "Can you help me find the Chinese translation for the psychological term '{0}'?",
    "What do you call the psychological term '{0}' in Chinese?",
    "What is the Chinese translation equivalent for the psychological term '{0}'?",
    "Can you convert the psychological term '{0}' into Chinese?",
    "Please render the psychological term '{0}' into Chinese.",
    "How do I say the psychological term '{0}' in Chinese?",
    "What is the Chinese word for the psychological term '{0}'?",
    "Could you translate the psychological term '{0}' into Chinese?",
    "What is the Chinese translation of the term '{0}' used in psychology?",
    "How can I express the psychological term '{0}' in Mandarin Chinese?",
    "What would be the Chinese equivalent term for the psychological term '{0}'?",
    "Please provide me with the Chinese translation for the term '{0}' in psychology.",
    "How is the term '{0}' in psychology translated into Chinese?",
    "Can you help me with the Chinese term for '{0}' in psychology?",
    "I would like to know the Chinese translation for the term '{0}' in psychology.",
    "What is the Mandarin Chinese translation for the term '{0}' used in psychology?",
    "Is there a Chinese term for '{0}' in psychology?",
    "How is '{0}' in psychology said in Chinese?",
    "What is the Mandarin translation for the psychological term '{0}'?",
    "Can you convert the term '{0}' used in psychology into Chinese?",
    "What would be the Chinese version of the term '{0}' in psychology?",
    "Could you please provide the Chinese translation for the term '{0}' in psychology?",
    "What is the Chinese translation for the expression '{0}' in psychology?",
    "How do you say the term '{0}' in psychology in Chinese?",
    "Please help me with the Chinese term for the expression '{0}' in psychology.",
    "What is the Chinese equivalent for the term '{0}' in psychology?",
    "How do they refer to '{0}' in psychology in Chinese?",
    "What is the Mandarin Chinese version of the psychological term '{0}'?",
    "Can you translate the phrase '{0}' used in psychology into Chinese?",
    "What is the Chinese translation of the concept '{0}' in psychology?",
    "How can I say the term '{0}' used in psychology in Mandarin Chinese?",
    "What would be the Chinese counterpart term for '{0}' used in psychology?",
    "Please provide me with the Chinese translation for the expression '{0}' in psychology.",
    "How is the term '{0}' in psychology translated in Chinese?",
    "Can you help me with the Chinese term for '{0}' used in psychology?",
    "I would like to know the Chinese translation for the expression '{0}' in psychology.",
    "What is the Mandarin Chinese translation for the expression '{0}' used in psychology?",
    "Is there a Chinese term for the concept '{0}' in psychology?",
    "How is '{0}' used in psychology said in Chinese?",
    "What is the Mandarin translation for the term '{0}' used in psychology?",
    "Can you convert the expression '{0}' used in psychology into Chinese?",
    "What would be the Chinese version of the concept '{0}' in psychology?",
    "Could you please provide the Chinese translation for the expression '{0}' in psychology?",
    "What is the Chinese translation for the phrase '{0}' used in psychology?",
    "How do you say the expression '{0}' in psychology in Chinese?",
    "Please help me with the Chinese term for the phrase '{0}' in psychology.",
    "What is the Chinese equivalent for the expression '{0}' in psychology?",
    "How do they refer to '{0}' in psychology in Chinese?",
    "What is the Mandarin Chinese version of the phrase '{0}' used in psychology?",
]

try:
    os.remove("datasets/vocabulary.jsonl")
except:
    pass

with open("datasets/vocabulary.jsonl", mode="a", encoding="utf-8") as file:
    with open("origin/vocabulary.csv", newline='', encoding='utf-8-sig') as translations:
        reader = csv.DictReader(translations)
        for row in reader:
            file.write(json.dumps({
                'messages': [
                    {
                        'role': 'system',
                        'content': system_message
                    },
                    {
                        'role': 'user',
                        'content': possible_questions[random.randint(0, len(possible_questions) - 1)].format(row["English"].lower())
                    },
                    {
                        'role': 'assistant',
                        'content': row['Chinese']
                    }
                ]
            }, ensure_ascii=False) + '\n')