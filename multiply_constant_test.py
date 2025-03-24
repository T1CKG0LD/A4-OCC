from paillier import Paillier
import gmpy2

phe = Paillier(1024)

def multiply_constant_test(phe):
    m1 = 42
    m2 = 3
    c1 = phe.encrypt(m1)
    n = phe.pk[0]
    
    powered_cipher = gmpy2.powmod(c1, m2, n**2)
    
    decrypted = phe.decrypt(powered_cipher)
    
    assert decrypted == (m1 * m2) % n
    print("Test de multiplication par constante réussi")

multiply_constant_test(phe)