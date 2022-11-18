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
        return a + b





