class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Hamming(metaclass=Singleton):
    def __init__(self):
        self.num_parity_bits = 0
        self.list_parity_bit_positions = []
    
    # find the number of parity bits
    # 2^r ≥ m + r + 1 
    # where, r = redundant bit, m = data bit
    def find_number_of_parity_bits(self, data):
        data_length = len(data)
        num_of_parity_bits = 1
        while 2**num_of_parity_bits < data_length + num_of_parity_bits + 1:
            num_of_parity_bits += 1
        
        return num_of_parity_bits


    # get a list of parity bit positions, given the number of parity bits
    def generate_list_parity_bit_positions(self, num_of_parity_bits):
        result = []
        for i in range(num_of_parity_bits): 
            result.append(pow(2, i))
        return result

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
        self.num_parity_bits = self.find_number_of_parity_bits(data)
        self.list_parity_bit_positions = self.generate_list_parity_bit_positions(self.num_parity_bits)
        data = self.create_bit_chain(data)
        return self.set_parity_bits(data)


    # decode 
    def decode_data(self, data):
        data = data.decode()
        error = self.verify_correctness(data)
        if error == 0:
            print("No error was detected.")
        else:
            print("Bit in positions", error, "is flipped!")

        data = self.remove_parity(data)
        message = (chr(int(data, 2)))
        print("\n[DECODE] Data:", data, "\nMessage:", message)
        return error

