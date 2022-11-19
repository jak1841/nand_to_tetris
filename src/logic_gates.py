"""

    Implementing low level logic gates

"""
class gate:
    def __init__(self):
        pass

    # 0, 0 -> 1
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 0
    # Given 2 single bit both in the form of string, returns a bit speceficed by nand operation
    def nand(self, a, b):
        if (a == "1" and b == "1"):
            return "0"
        return "1"

    # 0 -> 1
    # 1 -> 0
    # Given a single bit in the form of string, returns a bit specefied by not operation
    def not_(self, a):
        return self.nand(a, a)

    # 0, 0 -> 0
    # 0, 1, -> 0
    # 1, 0 -> 0
    # 1, 1 -> 1
    # Given 2 single bit both in the form of string, returns a bit specefied by and operation
    def and_(self, a, b):
        return self.not_(self.nand(a, b))

    # 0, 0 -> 0
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 1
    # Given 2 single bit both as string return a bit of the or operation
    def or_(self, a, b):
        return self.nand(self.not_(a), self.not_(b))

    # 0, 0 -> 0
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 0
    # Given 2 single bit both as string return a bit of the xor operation
    def xor(self, a, b):
        not_ab = self.and_(self.not_(a), b)
        b_nota = self.and_(self.not_(b), a)

        return self.or_(not_ab, b_nota)

    # a!sel or bsel -> 1
    # Given 2 single bit and a selector bit will return a bit of the multiplexor operation
    # sel = 0 -> output equal a
    # sel = 1 -> output equal b
    def multiplexor(self, a, b, sel):
        a_not_sel = self.and_(a, self.not_(sel))
        b_sel = self.and_(b, sel)
        return self.or_(a_not_sel, b_sel)

    # given a single input bit and a selector bit will return two bits of the form of string doing demultiplexor operation
    # in!sel -> a
    # insel -> b
    def demultiplexor(self, input, sel):
        a = self.and_(input, self.not_(sel))
        b = self.and_(input, sel)
        return [a, b]

    # Input:    2 Binary number(both length N), selector bit
    # Ouput:    Binary number
    # Mulitplexor but with n bit data.
    def n_bit_multipexor (self, a, b, sel):
        result = ""
        for x in range(len(a)):
            result += self.multiplexor(a[x], b[x], sel)

        return result

    # Input:    Binary number (length N), selector bit
    # Ouput:    List of two binary numbers (Length N), Where first Index = a, 2nd index = b.
    # Demultiplexor with n bit input
    def n_bit_demultplexor(self, input, sel):
        a = ""
        b = ""
        for x in input:
            result = self.demultiplexor(x, sel)
            a += result[0]
            b += result[1]

        return [a, b]

    # Input:    2 binary numbers (Length N)
    # output:   binary number (Length N)
    # xor of both binary number
    def n_bit_xor(self, a, b):
        result = ""
        for x in range(len(a)):
            result += self.xor(a[x], b[x])

        return result

    # Input: 2 binary numbers (Length N)
    # Ouput: binary number (Length N)
    # OR of two binary numbers
    def n_bit_or(self, a, b):
        result = ""
        for x in range(len(a)):
            result+= self.or_(a[x], b[x])

        return result

