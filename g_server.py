import socket
import random
import threading

HOST = "0.0.0.0"
PORT = 7777
BANNER = """
== Guessing Game v1.0 ==
Enter your guess:"""

def handle_client(conn, addr):
    guessme = random.randint(1, 100)
    print(f"New client connected: {addr}")
    conn.sendall(BANNER.encode())

    while True:
        try:
            client_input = conn.recv(1024)
            guess = int(client_input.decode().strip())
            print(f"User guess attempt: {guess}")
            if guess == guessme:
                conn.sendall(b"Correct Answer!")
                break
            elif guess > guessme:
                conn.sendall(b"Guess Lower!\nenter guess: ")
            elif guess < guessme:
                conn.sendall(b"Guess Higher!\nenter guess:")
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    conn.close()
    print(f"Client disconnected: {addr}")

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT}")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    server()
