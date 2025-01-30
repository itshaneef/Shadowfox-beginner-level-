import socket
import threading
from queue import Queue

def scan_port(host, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)      
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except Exception:
        pass

def worker(host, ports, open_ports):
    while not ports.empty():
        port = ports.get()
        scan_port(host, port, open_ports)
        ports.task_done()

 
def scan_ports(host, start_port, end_port, num_threads=50):
    open_ports = []
    ports = Queue()

    for port in range(start_port, end_port + 1):
        ports.put(port)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(host, ports, open_ports))
        thread.daemon = True    
        threads.append(thread)
        thread.start()

    ports.join()

    return sorted(open_ports)

if __name__ == "__main__":
    target_host = "testphp.vulnweb.com"

    try:
        resolved_ip = socket.gethostbyname(target_host)
        print(f"Scanning open ports on {target_host} ({resolved_ip})...")
    except socket.gaierror:
        print(f"Failed to resolve hostname: {target_host}")
        exit()

    open_ports = scan_ports(target_host, 1, 65535, num_threads=100)

    if open_ports:
        print("Open Ports:", open_ports)
    else:
        print("No open ports found.")
