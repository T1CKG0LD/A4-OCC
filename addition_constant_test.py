from paillier import Paillier
import gmpy2

phe = Paillier(1024)

def addition_constant_test(phe):
    m1 = 42
    m2 = 123
    c1 = phe.encrypt(m1)
    n, g = phe.pk
    
    g_m2 = gmpy2.powmod(g, m2, n**2)
    new_cipher = (c1 * g_m2) % (n**2)
    
    decrypted = phe.decrypt(new_cipher)
    
    assert decrypted == (m1 + m2) % n
    print("Test d'addition avec constante réussi")

addition_constant_test(phe)