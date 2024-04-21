# THIS WORKED TOO!

import socket
import time
import random

def guess_number():
    random.seed(int(time.time()-1.1))
    n = random.randint(1000000000000000, 10000000000000000-1)
    return n

def main():
    host = "challs.nusgreyhats.org"
    port = 31111

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            guess = str(guess_number())
            print(guess)
            s.sendall(guess.encode("utf-8") + b"\n")
            data = s.recv(2048).decode("utf-8")
            if "grey{" in data:
                print(data)
                break
            
if __name__ == "__main__":
    main()
