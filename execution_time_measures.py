import time
import matplotlib.pyplot as plt
from client import Client
from server import Server

def measure_execution_time():
    db_sizes = list(range(10, 101, 10))
    client_times = []
    server_times = []
    
    for db_size in db_sizes:
        index_to_retrieve = db_size // 2 
        
        start_time = time.time()
        client = Client()
        request = client.request(db_size, index_to_retrieve)
        public_key = client.pk
        client_time = time.time() - start_time
        client_times.append(client_time)
        
        server = Server(db_size)
        start_time = time.time()
        encrypted_answer = server.answer_request(request, public_key)
        server_time = time.time() - start_time
        server_times.append(server_time)
        
        _ = client.decrypt_answer(encrypted_answer)
    
    plt.figure(1)
    plt.plot(db_sizes, client_times, marker='x')
    plt.xlabel("Database size")
    plt.ylabel("Execution time (s)")
    plt.title("Impact of Database size on execution time on client side")
    plt.legend()
    plt.grid()
    plt.show()
    
    plt.figure(2)
    plt.plot(db_sizes, server_times, marker='x')
    plt.xlabel("Database size")
    plt.ylabel("Execution time (s)")
    plt.title("Impact of Database size on execution time on server side")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    measure_execution_time()

