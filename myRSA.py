from myMath import *

# retorna o totiente de n, λ(n), tal que como p e q são primos no RSA pode ser descrito como  λ(n) = lcm((p-1),(q-1))
def phi(p,q):
    return lcm((p-1),(q-1))

# retorna o N do RSA, o produto de p e q
def getN(p,q):
    return p*q

# define e retorna um valor pra e dado λ(n)
def getE(phi):
    while (True):
        e = random.randrange(2, phi)
        if (gcd(e, phi) == 1):
            return e    
        
#retorna o valor de d, o resultado do módulo inverso de e mod n       
def getD(e,n):
    return modinv(e,n)

#dados uma chave publica e m retorna um valor C que coresponde a m cripitografado 
def encript(publicKey,m):
    return pow(m,publicKey.e,publicKey.n) 

#dados uma chave privada e c retorna um valor M que coresponde a c decripitografado
def decript(privateKey,c):
    return pow(c,privateKey.d,privateKey.n) 


# Chinese remainder implementation

def getDp(d,p):
    return d % (p-1)

def getDq(d,q):
    return d % (q-1)

def getQinv(p,q):
    return modinv(q,p)

def decriptFAST(privateKey, m):
    m1 = pow(m,privateKey.dp,privateKey.p)  
    m2 = pow(m,privateKey.dq,privateKey.q)
    h = 0
    if(m2 > m1 ):
        print("So sad")
        h = (privateKey.qinv * ((m1 + ((privateKey.q/privateKey.p)*privateKey.p))-m2)) % privateKey.p
    else :
        h = (privateKey.qinv * (m1 +-m2)) % privateKey.p
    return (m2 + (privateKey.q * h)) % privateKey.n
        
#classe para a chave privada
class PrivateKey(object):
    dp = 0
    dq = 0
    qinv = 0
    p = 0
    q = 0
    d = 0
    n = 0
    
def makePrivateKey(p, q, n, d):
    pk = PrivateKey()
    pk.p = p
    pk.q = q
    pk.n = n
    pk.d = d
    pk.dp = getDp(d,p)
    pk.dq = getDq(d,q)
    pk.qinv = getQinv(p,q)
    return pk

#classe para a chave publica
class PublicKey(object):
    e = 0
    n = 0
    
def makePublicKey(e, n):
    pk = PublicKey()
    pk.e = e
    pk.n = n
    return pk