import json
from difflib import SequenceMatcher, get_close_matches
from connector import connector
data = json.load(open("data.json"))


c=connector()

def translate(w):
    if w not in data.keys() and w.lower() in data.keys():
        w=w.lower()
    elif w not in data.keys() and w.upper() in data.keys():
        w=w.upper()
    elif w not in data.keys() and w.capitalize() in data.keys():
        w=w.capitalize()
    if w in data:
        c.getWord(w)
    elif w not in data and len(get_close_matches(w,data.keys(),cutoff=0.8))>0 :
        yesorno=input(f"Did you mean { get_close_matches(w,data.keys(),cutoff=0.8)[0] }? y/n ")
        if yesorno.lower()=="y":
            similar=get_close_matches(w,data.keys())[0]
            return c.getWord(similar)
        elif yesorno.lower()=="n":
            print("Starting again ...")
            word = input("What is your word? : ")
            output = translate(word)
            if str(type(output))=="<class 'list'>":
                for (i,y) in enumerate(output,1):
                    print(i, y)
            else:
                print(output)
                ending=input("Will that be all? y/n : ")
                if ending =="y":
                    return "Thank you!"
                elif ending=="n":
                    scriptMain()
        
                #main = [ x for x in similar if SequenceMatcher(None,w,x).ratio()>0.75 ][0]
                #return data[main]
    else:
        return "This word does not exist! or Try to Capitalize the full word or just the direst Letter"
    
def scriptMain():
    word = input("What is your word? : ")

    output = translate(word)

    if str(type(output))=="<class 'list'>":
        for (i,y) in enumerate(output,1):
            print(i, y)
    else:
        print(output)
        ending=input("Will that be all? y/n : ")
        if ending =="y":
            return "Thank you!"
        elif ending=="n":
            scriptMain()
scriptMain()