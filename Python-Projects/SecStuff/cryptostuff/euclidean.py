from random import randrange


def gcd(a,b):
    if b == 0:
        return a
    return(b,a%b)


def prime_number():
    test_number = randrange(10,100)
    for i in range(2,test_number):
        if test_number % i == 0:
            return prime_number()
    return test_number