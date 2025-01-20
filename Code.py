import socket
import threading

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from {addr}: {data}")
        conn.sendall(data.upper())  # Enviamos el mensaje en mayúsculas

HOST = 'IP'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
