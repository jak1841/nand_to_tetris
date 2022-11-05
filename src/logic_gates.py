"""

    Implementing low level logic gates

"""
class gate:
    def __init__(self):
        pass

    # Given a 2 single bit both in the form of string, returns a bit speceficed by nand operation
    def nand(self, a, b):
        if (a == "1" and b == "1"):
            return "0"
        return "1"

    # Given a single bit in the form of string, returns a bit specefied by not operation
    def not_(self, a):
        return self.nand(a, a)


def main():
    print("start of a journey")
    pass

main()


