from utils import *
from Crypto.Util import number
import gmpy2

class Paillier:
    def __init__(self, bits):
        self.bits = bits
        self.keyGen(bits)
        
    def keyGen(self, bits):
        while True:
            p = number.getPrime(bits)
            q = number.getPrime(bits)
            n = p * q
            if gmpy2.gcd(n, (p-1)*(q-1)) == 1:
                break      
        g = n + 1
        lambda_val = (p-1) * (q-1)
        mu = gmpy2.invert(lambda_val, n)
        
        self.pk = (n, g)
        self.sk = (lambda_val, mu)

  
  
    def encrypt(self, message: int):
        n, g = self.pk
        if message < 0 or message >= n:
            raise ValueError("Message must be in range [0, n-1]")
        while True:
            r = number.getRandomRange(1, n)
            if gmpy2.gcd(r, n) == 1:
                break
        g_m = gmpy2.powmod(g, message, n**2)
        r_n = gmpy2.powmod(r, n, n**2)
        ciphertext = gmpy2.mul(g_m, r_n) % (n**2)
        return ciphertext


  
    def decrypt(self, ciphertext: int):
        n, g = self.pk
        lambda_val, mu = self.sk

        def L(x):
            return gmpy2.f_div(x-1, n)
        c_lambda = gmpy2.powmod(ciphertext, lambda_val, n**2)
        m = gmpy2.mul(L(c_lambda), mu) % n
        
        return int(m)
