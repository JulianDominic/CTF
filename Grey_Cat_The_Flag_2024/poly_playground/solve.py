# THIS WORKED !!!

import numpy as np
import socket

# roots = [1, 2]
# coefficients = np.poly(roots)
# print(",".join([str(int(i)) for i in coefficients]))

def main():
    host = "challs.nusgreyhats.org"
    port = 31113

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(4096).decode("utf-8")
            if "grey{" in data:
                print(data)
                break
            roots_line = data.split('\n')[-2]
            roots = [int(i) for i in roots_line.split(':')[1].strip().split(',')]
            coefficients = np.poly(roots)
            answer = ",".join([str(int(i)) for i in coefficients])
            print("coeff:", answer)
            s.sendall(answer.encode("utf-8") + b"\n")

if __name__ == "__main__":
    main()
