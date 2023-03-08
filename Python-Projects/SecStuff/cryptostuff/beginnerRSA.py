from math import gcd,sqrt,ceil,pow
from random import randint
import gmpy2

def calc_n(p,q):
    n = p * q
    return n

def calc_phi(p,q):
    phi = (p-1) * (q-1)
    return phi

def calc_e(n,phi):
    keys=[]
    for e in range(2,phi):
        if gcd(n,e) == 1 and gcd(phi,e) == 1:
            keys.append(e)
    
    return(keys[randint(0,len(keys)-1)])

def calc_d(phi,e):
    keys =[]
    for d in range(phi+1,phi*2):
        if (d*e % phi == 1) :
            keys.append(d)
    
    return(keys[randint(0,len(keys)-1)])

#using the euclidean algorithm
#format is a = bk + r
def calc_primes(n):
    a = ceil(sqrt(n))
    b = 0 
    count = 0 
    while True:
        if (a ** 2 - n) == (b ** 2):
            return ((a+b),(a-b))
        a +=1
        b = a ** 2 - n
        count += 1
        if count % 30000 == 0:
            print(a,b)





#N = a ** 2 - b ** 2 


n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857 #| calc_n(p,q)
#calc = calc_primes(n)
p =   1593021310640923782355996681284584012117
q =  521911930824021492581321351826927897005221

#print(p,q,p*q == n)
phi = calc_phi(p,q) 
e =  65537
d = calc_d(phi,e)
#pub_key = (e,n)
#priv_key = (d,n)
print(d,phi)
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
ans = (pow(c, d)) % n

print(ans)

print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))