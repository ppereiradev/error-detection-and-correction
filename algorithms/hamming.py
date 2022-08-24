"""
Approach: The idea is to first find the number of redundant bits which can be 
found by initializing r with 1 and then incrementing it by 1 each 
time while 2r is smaller than (m + r + 1) where m is 
the number of bits in the input message. Follow the below steps to solve the problem:

1. Initialize r by 1 and increment it by 1 until 2r is smaller than m+r+1.
2. Initialize a vector hammingCode of size r + m which will be the length of the output message.
3. Initialize all the positions of redundant bits with -1 by 
   traversing from i = 0 to r – 1 and setting hammingCode [2i – 1] = -1. 
   Then place the input message bits in all the positions where hammingCode[j]
   is not -1 in order where 0 <= j < (r + m).
4. Initialize a variable one_count with 0 to store the number of ones and then traverse from i = 0 to (r + m – 1).
5. If the current bit i.e., hammingCode[i] is not -1 then find the message 
   bit containing set bit at log2(i+1)th position by traversing 
   from j = i+2 to r+m by incrementing one_count by 1 if (j & (1<<x)) is not 0 and hammingCode[j – 1] is 1.
6. If for index i, one_count is even, set hammingCode[i] = 0 otherwise set hammingCode[i] = 1.
7. After traversing, print the hammingCode[] vector as the output message.
"""
class Hamming():
    def __init__(self):
        self.num_parity_bits = 0
        # find the number of parity bits
        # 2^r ≥ m + r + 1 
        # where, r = redundant bit, m = data bit
        self.list_parity_bit_positions = [1, 2, 4, 8]

    # create the bit positions first, set the parity bits to 0
    def create_bit_chain(self, data):
        for position in self.list_parity_bit_positions:
            data = data[:position-1] + "0" + data[position-1:]
        return data

    def set_parity_bits(self, data):
        data = list(data)
        
        for i in range(len(self.list_parity_bit_positions)):
            sum_aux = 0
            for j in range(i+1, len(data)):
                if j+1 & self.list_parity_bit_positions[i] == self.list_parity_bit_positions[i]:
                    sum_aux += int(data[j])

            if sum_aux % 2 == 0:
                data[self.list_parity_bit_positions[i]-1] = '0'
            else:
                data[self.list_parity_bit_positions[i]-1] = '1'

        return "".join(data)
    
    def verify_correctness(self, data):
        result = []
        for i in range(len(data)):
            if data[i] == '1':
                result.append(i+1)

        return self.xor(result)

    # XOR the list of numbers
    def xor(self, positions):
        res = 0
        for bit in positions:
            res = res ^ bit
        return res

    def remove_parity(self, data):
        data = list(data)
        for idx in self.list_parity_bit_positions:
            data[idx-1] = None

        data = [i for i in data if i is not None]
        return "".join(data)

    # encode 
    def encode_data(self, data):
        data = self.create_bit_chain(data)
        return self.set_parity_bits(data)

    # decode 
    def decode_data(self, data):
        data = data.decode()
        error = self.verify_correctness(data)
        if error == 0:
            print("\nNo error was detected.")
        else:
            print("\nBit in positions", error, "is flipped!")

        data = self.remove_parity(data)
        message = (chr(int(data, 2)))
        print("[BYTE DECODED] Data:", data, "\nMessage:", message)
        return error

