from json import dumps

_default_system_message__old = "Linga is a psychologist chatbot that can accurately translate the terminologies in literature in his area to Chinese."
default_system_message = 'You are a psychologist chatbot that can accurately translate the terminologies in literature in his area to Chinese.'
default_prompt_template = 'Now I will give you a paragraph of a psychological literature. Please focus on the psychological term and translate the everything in the paragraph into Chinese accurately and make the content more understandable and in line with the Chinese expression system, without changing the meaning of the original text. Please give me the best result: {0}'

def buildPrompt(question):
    return [
        {"role": "system", "content": default_system_message},
        {"role": "user", "content": question}
    ]

def buildLine(question, answer):
    return [
        {"role": "system", "content": default_system_message},
        {"role": "user", "content": question},
        {"role": "assistant", "content": answer}
    ]
    
def dumpSimple(obj):
    return dumps(obj, ensure_ascii=False)
    
def dumpLine(obj):
    return dumps({"messages": obj}, ensure_ascii=False) + "\n"

def removeReturn(string):
    return string.replace('\n', '')

def withoutReturn(array):
    return [x for x in array if x != '\n']

def splitByRegex(string, regex):
    parts = re.split(re.compile(regex), string)
    i = 0
    for word in re.findall(regex, string):
        parts[i] += word
        i += 1
    return parts
