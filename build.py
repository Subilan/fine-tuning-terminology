import csv
from random import randint
from json import dumps
from os import remove

possible_questions = [
    "What is the Chinese psychological translation of {0}?",
    "How do you say {0} in Chinese psychology?",
    "In Chinese psychology, what does {0} mean?",
    "Can you provide the psychological translation of {0} in Chinese?",
    "I would like to know the Chinese psychological equivalent of {0}.",
    "Please explain the psychological meaning of {0} in Chinese.",
    "What is the Chinese interpretation of {0} from a psychological perspective?",
    "Could you tell me how {0} is psychologically translated in Chinese?",
    "What does {0} represent in Chinese psychology?",
    "What is the meaning of {0} in the context of Chinese psychology?",
    "Is there a psychological translation for {0} in Chinese?",
    "What is the Chinese term for {0} in the field of psychology?",
    "What is the psychological connotation of {0} in Chinese?",
    "How is {0} psychologically understood in the Chinese language?",
    "What is the Chinese psychological equivalent for {0}?",
    "What is the psychological significance of {0} in Chinese?",
    "If {0} is to be translated into Chinese psychology, what would it be?",
    "Can you explain how {0} is perceived in Chinese psychology?",
    "What is the psychological interpretation of {0} in the Chinese language?",
    "I'm trying to grasp the psychological translation of {0} in Chinese.",
    "Can you provide insights into the psychological meaning of {0} in Chinese?",
    "What is the Chinese psychological term for {0}?",
    "How is {0} construed from a psychological perspective in Chinese?",
    "In Chinese psychology, what is the interpretation of {0}?",
    "What would be the psychological equivalent of {0} in Chinese?",
    "What does {0} signify in the realm of Chinese psychology?",
    "How is {0} psychologically defined in the Chinese language?",
    "What is the psychological understanding of {0} in Chinese?",
    "What is the Chinese version of {0} from a psychological standpoint?",
    "Could you please elucidate the psychological translation of {0} in Chinese?",
    "What is the Chinese psychological interpretation of {0}?",
    "What is {0}'s meaning in Chinese psychology?",
    "Can you explain how {0} is understood psychologically in Chinese?",
    "What is the psychological connotation of {0} in the Chinese language?",
    "How is {0} perceived in terms of Chinese psychology?",
    "What is the psychological interpretation of {0} in Chinese?",
    "Can you explain the Chinese psychological equivalent of {0}?",
    "What is the psychological significance of {0} in the Chinese language?",
    "If we interpret {0} in the field of Chinese psychology, what meaning does it carry?",
    "What is the term for {0} in Chinese psychology?",
    "How is {0} psychologically understood according to Chinese thinking?",
    "In the context of Chinese psychology, what is the interpretation of {0}?",
    "What is {0}'s psychological equivalent in Chinese?",
    "What does {0} symbolize in Chinese psychology?",
    "How is {0} defined psychologically in the Chinese language?",
    "What is the psychological understanding of {0} in the Chinese language?",
    "Can you explain the psychological translation of {0} in Chinese?",
    "What is the Chinese psychological interpretation of {0}?",
    "What is {0}'s meaning in the field of Chinese psychology?",
    "Can you explain how {0} is perceived psychologically in Chinese?",
    "What is the psychological connotation of {0} in Chinese?",
    "How is {0} viewed from a psychological perspective in Chinese?",
    "What is the psychological interpretation of {0} in the Chinese language?",
    "What is the Chinese psychological term used for {0}?",
    "What is the significance of {0} in Chinese psychology?",
    "If we relate {0} to Chinese psychology, what does it represent?",
    "What is the Chinese psychological term for {0}?",
    "How is {0} psychologically understood in the Chinese language?",
    "In Chinese psychology, what is the interpretation of {0}?",
    "What would be the psychological equivalent of {0} in Chinese?",
    "What does {0} signify in Chinese psychology?",
    "How is {0} defined psychologically in the Chinese language?",
    "What is the psychological understanding of {0} in Chinese?",
    "What is the Chinese version of {0} from a psychological standpoint?",
    "Can you explain the psychological translation of {0} in Chinese?",
    "What is the Chinese psychological interpretation of {0}?",
    "What is {0}'s meaning in the field of Chinese psychology?",
    "Can you explain how {0} is perceived psychologically in Chinese?",
    "What is the psychological connotation of {0} in Chinese?",
    "How is {0} viewed from a psychological perspective in Chinese?",
    "What is the psychological interpretation of {0} in the Chinese language?",
    "What is the Chinese psychological term used for {0}?",
    "What is the significance of {0} in Chinese psychology?",
    "If we relate {0} to Chinese psychology, what does it represent?",
    "What is the Chinese psychological term for {0}?",
    "How is {0} psychologically understood in the Chinese language?",
    "In Chinese psychology, what is the interpretation of {0}?",
    "What would be the psychological equivalent of {0} in Chinese?",
    "What does {0} signify in Chinese psychology?",
    "How is {0} defined psychologically in the Chinese language?",
    "What is the psychological understanding of {0} in Chinese?",
    "What is the Chinese version of {0} from a psychological standpoint?",
    "Can you explain the psychological translation of {0} in Chinese?",
    "What is the Chinese psychological interpretation of {0}?",
    "What is {0}'s meaning in the field of Chinese psychology?",
    "Can you explain how {0} is perceived psychologically in Chinese?",
    "What is the psychological connotation of {0} in Chinese?",
    "How is {0} viewed from a psychological perspective in Chinese?",
    "What is the psychological interpretation of {0} in the Chinese language?",
    "What is the Chinese psychological term used for {0}?",
    "What is the significance of {0} in Chinese psychology?",
    "If we relate {0} to Chinese psychology, what does it represent?"
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
