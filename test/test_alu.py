import unittest
import sys

# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')

from arithemtic_logic_unit import alu as a
alu = a()

class Test(unittest.TestCase):
    def test_half_adder(self):
        self.assertEqual("00", alu.half_adder("0", "0"))
        self.assertEqual("01", alu.half_adder("1", "0"))
        self.assertEqual("01", alu.half_adder("0", "1"))
        self.assertEqual("10", alu.half_adder("1", "1"))

    def test_full_adder(self):
        self.assertEqual("00", alu.full_adder("0", "0", "0"))
        self.assertEqual("01", alu.full_adder("1", "0", "0"))
        self.assertEqual("01", alu.full_adder("0", "1", "0"))
        self.assertEqual("01", alu.full_adder("0", "0", "1"))
        self.assertEqual("10", alu.full_adder("1", "1", "0"))
        self.assertEqual("10", alu.full_adder("1", "0", "1"))
        self.assertEqual("10", alu.full_adder("0", "1", "1"))
        self.assertEqual("11", alu.full_adder("1", "1", "1"))

    def test_adder_16_bit (self):
        a = "0000000000000000"
        b = "0000000000000001"
        self.assertEqual("0000000000000001", alu.adder_16_bit(a, b))

        a = "1111111111111111"
        b = "0000000000000001"
        self.assertEqual("0000000000000000", alu.adder_16_bit(a, b))

        a = "1111111111111111"
        b = "0000000000000001"
        self.assertEqual("0000000000000000", alu.adder_16_bit(a, b))

        a = "1010101010101010"
        b = "0101010101010101"
        self.assertEqual("1111111111111111", alu.adder_16_bit(a, b))


        a = "0101010101111000"
        b = "1100110000000000"
        self.assertEqual("0010000101111000", alu.adder_16_bit(a, b))

        a = "1010010101010101"
        b = "1111111100001111"
        self.assertEqual("1010010001100100", alu.adder_16_bit(a, b))





if __name__ == '__main__':
    unittest.main()