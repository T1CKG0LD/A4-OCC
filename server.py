import random
from utils import *

class Server:
    def __init__(self, db_size):
        if db_size <= 0:
            raise ValueError("Database size must be positive")
        self.db = [random.randint(1, 2**16) for _ in range(db_size)]



    def answer_request(self, request_vector, client_pk):
        n, g = client_pk
        if len(request_vector) != len(self.db):
            raise ValueError("Request size doesn't match with database size")
        
        encrypted_answer = 1
        for db_val, encrypted_bit in zip(self.db, request_vector):
            term = pow(encrypted_bit, db_val, n**2)
            encrypted_answer = (encrypted_answer * term) % (n**2)
        
        return encrypted_answer
