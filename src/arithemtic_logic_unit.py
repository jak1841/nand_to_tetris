from logic_gates import gate

class alu():
    def __init__(self):
        self.gate = gate()
        pass

    # Given two binary bits as strings adds them and returns a string of sum and carry bit
    # return is carry bit followed by sum bit
    # 0, 0 -> 00
    # 0, 1 -> 01
    # 1, 0 -> 01
    # 1, 1 -> 10
    def half_adder(self, a, b):
        carry = self.gate.and_(a, b)
        summ = self.gate.xor(a, b)
        return carry + summ

    # Given 2 binary bits and carry bit as strings adds them and returns a string of sum and carry bit
    # return is carry bit followed by sum bit
    # 0, 0, 0 -> 00
    #
    def full_adder(self, a, b, c):
        carry1, summ = self.half_adder(a, b)
        carry2, summ = self.half_adder(summ, c)

        carry = self.gate.or_(carry1, carry2)
        return carry + summ


    # Given 2 16 bits binary numbers will return the addition of those two numbers
    # Does not handle overflow
    def adder_16_bit(self, a, b):
        carry_bit = 0
        result = "0000000000000000"
        for x in range(16):
            carry_bit, summ = self.full_adder(b[16 - x], a[16 - x], carry_bit)
            result[16 - x] = summ

        return result
        





