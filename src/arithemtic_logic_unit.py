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
        result = ["0" for x in range(16)]
        for x in range(16):
            carry_bit, summ = self.full_adder(b[15 - x], a[15 - x], carry_bit)
            result[15 - x] = summ

        return "".join(result)

    # Given a 16 bit binary number represented as a string will return the increment of that number
    # Does not handle overflow
    def increment_16_bit(self, a):
        one = "0000000000000001"
        return self.adder_16_bit(one, a)

    # Inputs: x[16] y[16]       Two 16-bit data inputs
    #         zx,               Zero the x input
    #         nx,               negate the x input
    #         zy,               zero the y input
    #         ny,               negate the y input
    #         f,                Function code: 1 for Add, 0 for And
    #         no,               negate the output

    # Outputs:  out[16]         16 bit data output
    #           zr,             true iff out = 0
    #           ng,             true iff out < 0

    def alu_16_bit(self, x, y, zx, nx, zy, ny, f, no):
        zeroed_x = self.gate.n_bit_xor(x, x)
        x1 = self.gate.n_bit_multipexor(x, zeroed_x, zx)
        negated_x = self.gate.n_bit_not(x1)
        x2 = self.gate.n_bit_multipexor(x1, negated_x)

        zeroed_y = self.gate.n_bit_xor(y, y)
        y1 = self.gate.n_bit_multipexor(y, zeroed_y)
        negated_y = self.gate.n_bit_not(y1)
        y2 = self.gate.n_bit_multipexor(y1, negated_y)

        added_x_y = self.adder_16_bit(x2, y2)
        and_x_y = self.gate.n_bit_and(x2, y2)

        output  = self.gate.n_bit_multipexor(and_x_y, added_x_y)
        negated_output = self.gate.n_bit_not(output)

        out = self.gate.n_bit_multipexor(output, negated_output)

    









