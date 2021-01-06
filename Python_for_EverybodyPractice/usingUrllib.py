from urllib import request,parse,error


fhand = request.urlopen('https://google.com')
for line in fhand:
    try:
        print(line.decode().strip())
    except:
        pass
    finally:
        print("Brilliant!")