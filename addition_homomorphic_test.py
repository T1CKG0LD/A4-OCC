from paillier import Paillier

phe = Paillier(1024)

def test_homomorphic_addition(phe):
    m1 = 42
    m2 = 123
    c1 = phe.encrypt(m1)
    c2 = phe.encrypt(m2)
    
    n = phe.pk[0]
    product = (c1 * c2) % (n**2)
    
    decrypted = phe.decrypt(product)
    
    assert decrypted == (m1 + m2) % n
    print("Test d'addition homomorphique réussi")

test_homomorphic_addition(phe)
