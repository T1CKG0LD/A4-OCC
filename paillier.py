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





"""----------Test of homomorphic addition------------"""
    def test_homomorphic_addition(self):
        m1 = 42
        m2 = 123
        c1 = self.encrypt(m1)
        c2 = self.encrypt(m2)
        
        n = self.pk[0]
        product = (c1 * c2) % (n**2)
        
        decrypted = self.decrypt(product)
        
        assert decrypted == (m1 + m2) % n
        print("Homomorphic addition test passed")





"""----------Test of addition with a constant------------"""
    def test_addition_constant(self):
        m1 = 42
        m2 = 123
        c1 = self.encrypt(m1)
        n, g = self.pk
        
        g_m2 = gmpy2.powmod(g, m2, n**2)
        new_cipher = (c1 * g_m2) % (n**2)
        
        decrypted = self.decrypt(new_cipher)
        
        assert decrypted == (m1 + m2) % n
        print("Test d'addition avec constante réussi")





"""----------Test of multiplication by a constant------------"""
    def test_multiply_constant(self):
        m1 = 42
        m2 = 3
        c1 = self.encrypt(m1)
        n = self.pk[0]
        
        powered_cipher = gmpy2.powmod(c1, m2, n**2)
        
        decrypted = self.decrypt(powered_cipher)
        
        assert decrypted == (m1 * m2) % n
        print("Test de multiplication par constante réussi")





"""----------Application with 1024 bits------------"""
if __name__ == "__main__":
    phe = Paillier(1024)
    phe.test_addition_constant()
    phe.test_homomorphic_addition()
    phe.test_multiply_constant()
