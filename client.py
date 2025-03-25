from paillier import Paillier
from utils import *

class Client:

    def __init__(self, bits=1024):
        self.phe = Paillier(bits)  
        self.pk = self.phe.pk     
        self.sk = self.phe.sk     
        
        print(f"Client initialisé avec clé Paillier {bits}-bits")
        print(f"Clé publique (n,g): {self.pk}")



    def request(self, db_size, index):
        if index < 0 or index >= db_size:
            raise ValueError(f"Index {index} hors limites (taille DB: {db_size})")
        
        request_vector = []
        for j in range(db_size):
            message = 1 if j == index else 0
            encrypted_bit = self.phe.encrypt(message)
            request_vector.append(encrypted_bit)
        
        print(f"Requête PIR générée pour index {index}")
        return request_vector



    def decrypt_answer(self, encrypted_answer):
        decrypted_value = self.phe.decrypt(encrypted_answer)
        
        print(f"Réponse serveur déchiffrée: {decrypted_value}")
        return decrypted_value