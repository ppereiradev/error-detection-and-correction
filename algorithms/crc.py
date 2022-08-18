class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CRC(metaclass=Singleton):

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