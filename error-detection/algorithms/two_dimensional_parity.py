"""
In this technique, the sender appends an extra parity bit to the message.
If the total number of ones in the bit sequence is odd, 1 is added as a parity bit.
And, if it is even, 0 acts as a parity bit.

During transmission or storage, if an error alters the number of bits,
the parity bit will be used to identify whether there is an error or not.
"""
class TwoDimensionalParity:
    def encode_even_data(self, data):
        pass

    def decode_even_data(self, data):
        pass

