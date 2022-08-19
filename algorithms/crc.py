"""
# Sender Side (Generation of Encoded Data from Data and Generator Polynomial (or Key)):

1. The binary data is first augmented by adding k-1 zeros in the end of the data
2. Use modulo-2 binary division to divide binary data by the key and store remainder of division.
3. Append the remainder at the end of the data to form the encoded data and send the same

# Receiver Side (Check if there are errors introduced in transmission):
Perform modulo-2 division again and if the remainder is 0, then there are no errors. 

Modulo 2 Division:
The process of modulo-2 binary division is the same as the familiar division process we use for decimal numbers. Just that instead of subtraction, we use XOR here.

1. In each step, a copy of the divisor (or data) is XORed with the k bits of the dividend (or key).
2. The result of the XOR operation (remainder) is (n-1) bits, which is used for the next step after 1 extra bit is pulled down to make it n bits long.
3. When there are no bits left to pull down, we have a result. The (n-1)-bit remainder which is appended at the sender side.
"""
class CRC():

    def xor(self, a, b):
        result = []

        for i in range(1, len(b)):
            if a[i] == b[i]:
                result.append('0')
            else:
                result.append('1')

        return ''.join(result)


    def mod2div(self, divident, divisor):
        pick = len(divisor)

        # Slicing the divident to appropriate
        # length for particular step
        tmp = divident[0: pick]

        while pick < len(divident):

            if tmp[0] == '1':

                # replace the divident by the result
                # of XOR and pull 1 bit down
                tmp = self.xor(divisor, tmp) + divident[pick]

            else: # If leftmost bit is '0'
                # If the leftmost bit of the dividend (or the
                # part used in each step) is 0, the step cannot
                # use the regular divisor; we need to use an
                # all-0s divisor.
                tmp = self.xor('0' * pick, tmp) + divident[pick]

            # increment pick to move further
            pick += 1

        # For the last n bits, we have to carry it out
        # normally as increased value of pick will cause
        # Index Out of Bounds.
        if tmp[0] == '1':
            tmp = self.xor(divisor, tmp)
        else:
            tmp = self.xor('0' * pick, tmp)

        checkword = tmp
        return checkword

    # Function used at the receiver side to decode
    # data received by sender
    def decode_data(self, data, key):
        l_key = len(key)

        # Appends n-1 zeroes at end of data
        appended_data = data.decode() + '0' * (l_key-1)
        remainder = self.mod2div(appended_data, key)

        return remainder

    def encode_data(self, data, key):
        l_key = len(key)

        # Appends n-1 zeroes at end of data
        appended_data = data + '0'*(l_key-1)
        remainder = self.mod2div(appended_data, key)

        # Append remainder in the original data
        codeword = data + remainder
        return codeword