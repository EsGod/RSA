import math 
import random

#Retorna o GCD ( maior divisor comum) entre dois números
def gcd(x, y):  
    while(y):
     x, y = y, x % y  
    return x

# Retorna o LCM( menor multiplo comum) entre dois núimeros
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

# usa uma implementação do Extended Euclidean algorithm afim de calcular o módulo inverso de a módulo m
def egcd(e, phi):
      
    if e == 0:
        return (phi, 0, 1)
    else:
        g, y, x = egcd(phi % e, e)
        return (g, x - (phi // e) * y, y)
    
# Retorna o módulo inverso de a mod M
def modinv(e, phi):
      
    g, x, y = egcd(e, phi)
    return x % phi
    
