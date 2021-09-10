import math 
import random

#concatena chars em uma string
def stringbuilder(s):  
    new = ""
    for x in s:
        new += x 
    return new

#retorna um random em um determinado intervalo de expoentes na base 10 , eg: 10 á  10000000
def rngB10(expini,expend):
      return random.randrange((10**expini), (10**expend))