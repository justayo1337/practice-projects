import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))

def translate(w):
    if w not in data.keys() and w.lower() in data.keys():
        w=w.lower()
    elif w not in data.keys() and w.upper() in data.keys():
        w=w.upper()
    elif w not in data.keys() and w.capitalize() in data.keys():
        w=w.capitalize()
    if w in data:
        return data[w]
    elif w not in data and len(get_close_matches(w,data.keys(),cutoff=0.9))>0 :
        yesorno=input(f"Did you mean { get_close_matches(w,data.keys(),cutoff=0.9)[0] }? y/n ")
        if yesorno=="y":
            similar=get_close_matches(w,data.keys())[0]
            return data[similar]
        else:
            print("Starting again ...")
            word = input("What is your word? : ")
            output = translate(word)

            if str(type(output))=="<class 'list'>":
                for (i,y) in enumerate(output,1):
                    print(i, y)
            else:
                print(output)
        
                #main = [ x for x in similar if SequenceMatcher(None,w,x).ratio()>0.75 ][0]
                #return data[main]
    else:
        return "This word does not exist! or Try to Capitalize the full word or just the direst Letter"
    

word = input("What is your word? : ")

output = translate(word)

if str(type(output))=="<class 'list'>":
    for (i,y) in enumerate(output,1):
        print(i, y)
else:
    print(output)