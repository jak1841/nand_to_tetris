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

def main():
    print("start of a journey")
    pass

main()


