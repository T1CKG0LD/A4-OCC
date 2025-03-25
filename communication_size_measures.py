import sys
import matplotlib.pyplot as plt
from client import Client
from server import Server

def measure_execution_time():
    db_sizes = list(range(10, 101, 10))
    client_to_server_sizes = []
    server_to_client_sizes = []
    
    for db_size in db_sizes:
        index_to_retrieve = db_size // 2  # Arbitrary choice of index
        
        # Communication size measure Client to Server
        client = Client()
        request = client.request(db_size, index_to_retrieve)
        public_key = client.pk
        client_to_server_size = sum(sys.getsizeof(enc) for enc in request) + sys.getsizeof(public_key)
        client_to_server_sizes.append(client_to_server_size)
        
        # Communication size measure Server to Client
        server = Server(db_size)
        encrypted_answer = server.answer_request(request, public_key)
        server_to_client_size = sys.getsizeof(encrypted_answer)
        server_to_client_sizes.append(server_to_client_size)
    
    # Curves
    plt.figure(1)
    plt.plot(db_sizes, client_to_server_sizes, marker='x')
    plt.xlabel("Database size")
    plt.ylabel("Communication size")
    plt.title("Impact of Database size on communication size Client to Server")
    plt.legend()
    plt.grid()
    plt.show()
    
    plt.figure(2)
    plt.plot(db_sizes, server_to_client_sizes, marker='x')
    plt.xlabel("Database size")
    plt.ylabel("Communication size")
    plt.title("Impact of Database size on communication size Server to Client")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    measure_execution_time()

