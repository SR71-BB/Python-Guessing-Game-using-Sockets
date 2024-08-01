import socket

HOST = "10.125.41.154"
PORT = 7777

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            banner = s.recv(1024).decode().strip()
            print(banner)

            while True:
                user_input = input("").strip()
                s.sendall(user_input.encode())
                reply = s.recv(1024).decode().strip()
                print(reply)
                if "Correct" in reply:
                    break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    client()
