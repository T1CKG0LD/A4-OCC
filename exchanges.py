from client import Client
from server import Server

def main():
    # Size of the db
    db_size = 50
    index_to_retrieve = 10  # Index the client wish to retrieve

    # Creation of the client and the server
    client = Client()
    server = Server(db_size)
    
    # The client generates the request
    request = client.request(db_size, index_to_retrieve)
    public_key = client.pk

    
    # The server answers to the request
    encrypted_answer = server.answer_request(request, public_key)
    
    # The client decrypts the answer
    retrieved_value = client.decrypt_answer(encrypted_answer)
    
    # Check
    assert retrieved_value == server.db[index_to_retrieve], "Error : incorrect value retrieved !"
    print(f"Test succeeded : the value retrieved ({retrieved_value}) corresponds to the one from the server.")

if __name__ == "__main__":
    main()
