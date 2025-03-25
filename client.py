from paillier import Paillier
from utils import *

class Client:

    def __init__(self, bits=1024):
        self.phe = Paillier(bits)  
        self.pk = self.phe.pk     
        self.sk = self.phe.sk     
        
        print(f"Paillier key {bits}-bits")
        print(f"Public key (n,g): {self.pk}")



    def request(self, db_size, index):
        if index < 0 or index >= db_size:
            raise ValueError(f"Index {index} out of limits (Database size : {db_size})")
        
        request_vector = []
        for j in range(db_size):
            message = 1 if j == index else 0
            encrypted_bit = self.phe.encrypt(message)
            request_vector.append(encrypted_bit)
        
        print(f"PIR request generated for index {index}")
        return request_vector



    def decrypt_answer(self, encrypted_answer):
        decrypted_value = self.phe.decrypt(encrypted_answer)
        
        print(f"Decrypted server response : {decrypted_value}")
        return decrypted_value
