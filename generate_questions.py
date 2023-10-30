from fn import default_prompt_template

lines = open("translations/separated.txt", mode='r').readlines()

lines_to_write = []

index = 0
for l in lines:
    if index % 2 == 0:
        lines_to_write.append(default_prompt_template.format(l))
    index += 1

open("to_translate.txt", mode='w').writelines(lines_to_write)