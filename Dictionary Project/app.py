import json
data = json.load(open("data.json"))

def translate(word):
    try:
        return data[word]
    except KeyError :
        return "This word does not exist!"
    

word = input("What is your word? : ")

print(translate(word))