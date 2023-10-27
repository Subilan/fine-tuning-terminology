from json import dumps

def withRoles(question, answer):
    return [
        {"role": "system", "content": "Linga is a psychologist chatbot that can accurately translate the terminologies in literature in his area to Chinese."},
        {"role": "user", "content": question},
        {"role": "assistant", "content": answer}
    ]
    
def toJsonl(obj):
    return dumps({"messages": obj}, ensure_ascii=False) + "\n"

def removeReturn(string):
    return string.replace('\n', '')