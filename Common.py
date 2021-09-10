import math 
import random
from BailliePSW import *

#concatena chars em uma string
def stringbuilder(s):  
    new = ""
    for x in s:
        new += x 
    return new

#retorna um random em um determinado intervalo de expoentes na base 10 , eg: 10 á  10000000
def rngB10(expini,expend):
      return random.randrange((10**expini), (10**expend))

#retorna um random em um determinado intervalo de expoentes na base 10 , eg: 10 á  10000000
def rngB2(expini,expend):
      return random.randrange((2**expini), (2**expend))
    
#retona um geradorr de numeros primos baseado na Sieve of Eratosthenes
def gen_primes():   
    D = {}      
    q = 2    
    while True:
        if q not in D:            
            yield q
            D[q * q] = [q]
        else:           
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1    
    
def verifyPrimeBrute(n):
    sqt = (int(math.sqrt(n)) +1)
    old = 0
    for p in gen_primes():
        
        if(p > old*10):
            print(p)
            old = p
        if(n % p == 0): return k == n
        if(p > sqt): return True
        
    
def PrimeRNG(ie,ee):    
        return next_prime(rngB2(ie,ee))    
