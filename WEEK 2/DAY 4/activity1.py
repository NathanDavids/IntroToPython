import re

def remove_number(text):
    result = re.sub(r'[0-4,6-9]', '', text)
    return result

text = input("Please enter any random text: ")
result = remove_number(text)
print(result)