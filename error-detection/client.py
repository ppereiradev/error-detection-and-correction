# Import socket module
import socket
import argparse
from algorithms.crc import CRC
from algorithms.hamming import Hamming
from algorithms.parity import Parity

class Client:
    def __init__(self):
        self.parity = Parity()
        self.crc = CRC()
        self.hamming = Hamming()

    def encode_data_parity(self, data):
        return self.parity.encode_odd_data(data)

    def encode_data_crc(self, data):
        key = "1001"
        return self.crc.encode_data(data, key)

    def encode_data_hamming(self, data):
        return self.hamming.encode_data(data)



if __name__ == '__main__':

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--algorithm", required=True, type=str,
        help="The algorithm to detect or correct error (types supported: parity, crc, hamming, reed).")
    args = vars(ap.parse_args())

    # Create a socket object
    socket_client = socket.socket()

    # Define the port on which you want to connect
    port = 12346

    # connect to the server on local computer
    socket_client.connect(('127.0.0.1', port))

    client_obj = Client()
    input_string = input("Enter data you want to send-> ")
    #s.sendall(input_string)

    data = [format(ord(x), 'b') for x in input_string]
    print("Entered data in binary format :", "".join(data))

    if args["algorithm"] == 'parity':
        ans = client_obj.encode_data_parity(data)

        print("Encoded data to be sent to server in binary format :", ans)
        socket_client.sendto(ans.encode(),('127.0.0.1', port))

        # receive data from the server
        print("Received feedback from server :",socket_client.recv(1024).decode())
        # close the connection
        socket_client.close()

    elif args["algorithm"] == 'crc':
        ans = ''
        for i in range(len(data)):
            ans += client_obj.encode_data_crc(data[i])

        print("Encoded data to be sent to server in binary format :", ans)
        socket_client.sendto(ans.encode(),('127.0.0.1', port))

        # receive data from the server
        print("Received feedback from server :",socket_client.recv(1024).decode())
        # close the connection
        socket_client.close()

    elif args["algorithm"] == 'hamming':
        ans = ''
        for i in range(len(data)):
            ans += client_obj.encode_data_hamming(data[i])

        print("Encoded data to be sent to server in binary format :", ans)
        socket_client.sendto(ans.encode(),('127.0.0.1', port))

        # receive data from the server
        print("Received feedback from server :",socket_client.recv(1024).decode())
        # close the connection
        socket_client.close()
