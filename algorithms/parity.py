"""
To compute the parity bit, we have to add all the digits together.

If we have error detection using odd parity, the receiver verify the parity
of the sum of digits that he or she received. If the result is odd, no error was detected,
if the parity is even, then an error was detected.
"""
class Parity:
    def find_parity(self, data):
        parity = [int(i) for i in list(format(ord(data), 'b'))]
        if sum(parity) % 2 == 0:
            return "".join(str(i) for i in parity) + " has even parity"
        else:
            return "".join(str(i) for i in parity) + " has odd parity"

    def has_odd_parity(self, data):
        parity = [int(i) for i in list(data)]
        if sum(parity) % 2 == 0:
            print("Even parity, error detected!")
            return False
        else:
            print("Odd parity, therefore no error detected.")
            return True

    def encode_data(self, data):
        parity = [int(i) for i in list(data)]
        if sum(parity) % 2 == 0:
            parity.insert(0, '1')

        return "".join(str(i) for i in parity)
            
    def decode_data(self, data):
        data = data.decode()
        return self.has_odd_parity(data)