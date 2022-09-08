# First of all import the socket library
import socket
import argparse
from algorithms.crc import CRC
from algorithms.hamming import Hamming
from algorithms.parity import Parity

class Server:
    def __init__(self):
        self.parity = Parity()
        self.crc = CRC()
        self.hamming = Hamming()

    def decode_data_parity(self, data):
        ans = self.parity.has_odd_parity(data)
        
        has_error = ans
        self.send_message_to_client(data, has_error)

    def decode_data_crc(self, data):
        key = "1001"
        ans = []
        
        for i in range(len(data)//10):
            ans.append(self.crc.decode_data(data[i*10:(i+1)*10], key))

        print("Remainder after decoding is-> ", ans)
        # If remainder is all zeros then no error occurred
        temp = "0" * (len(key) - 1)

        has_error = False
        for i in range(len(ans)):
            if ans[i] != temp:
                has_error = True
            
        self.send_message_to_client(data, has_error)

    def decode_data_hamming(self, data):
        ans = []
        
        for i in range(len(data)//11):
            ans.append(self.hamming.decode_data(data[i*11:(i+1)*11]))
        
        has_error = any(ans)
        self.send_message_to_client(data, has_error)

    def send_message_to_client(self, data, has_error):
        if has_error:
            client.sendto(("Error in data").encode(), ('127.0.0.1', 12345))
        else:
            client.sendto(("THANK you!\nData -> " + data.decode() +
                    " Received No error FOUND").encode(), ('127.0.0.1', 12345))


if __name__ == '__main__':

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--algorithm", required=True, type=str, 
        help="The algorithm to detect or correct error (types supported: parity, crc, hamming, reed).")
    args = vars(ap.parse_args())
    
    try:
        # Creating Socket
        socket_server = socket.socket()
        print("Socket successfully created")

        # reserve a port on your computer in our
        # case it is 12345 but it can be anything
        port = 12345
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.bind(('', port))
        print("socket binded to %s" % (port))
        # put the socket into listening mode
        socket_server.listen(5)
        print("socket is listening")

        client, addr = socket_server.accept()
        print('Got connection from', addr)

        
        while True:
            # Get data from client
            data = client.recv(1024)
            print("Received encoded data in binary format:", data.decode())
            
            if not data:
                break
            
            server_obj = Server()
            if args["algorithm"] == 'parity':
                server_obj.decode_data_parity(data)

            elif args["algorithm"] == 'crc':
                server_obj.decode_data_crc(data)

            elif args["algorithm"] == 'hamming':
                server_obj.decode_data_hamming(data)


    except KeyboardInterrupt:
        print("\n\nShutdown...")


