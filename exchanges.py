from client import Client
from server import Server

def main():
    db_size = 50
    index_to_retrieve = 10  
    
    client = Client()
    server = Server(db_size)

    request = client.request(db_size, index_to_retrieve)
    public_key = client.pk
    encrypted_answer = server.answer_request(request, public_key)
    retrieved_value = client.decrypt_answer(encrypted_answer)
    
    print(f"Test succeeded : the value retrieved ({retrieved_value}) corresponds to the one from the server.")

if __name__ == "__main__":
    main()
