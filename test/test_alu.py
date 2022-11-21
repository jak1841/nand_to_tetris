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

    def test_incrementer_16_bit (self):
        a = "1010101101101011"
        self.assertEqual("1010101101101100", alu.increment_16_bit(a))

        a = "1110010101011111"
        self.assertEqual("1110010101100000", alu.increment_16_bit(a))

        a = "1111111111111111"
        self.assertEqual("0000000000000000", alu.increment_16_bit(a))

        a = "0000000000000000"
        self.assertEqual("0000000000000001", alu.increment_16_bit(a))

        a = "1011101010110010"
        self.assertEqual("1011101010110011", alu.increment_16_bit(a))

        a = "1111111101111000"
        self.assertEqual("1111111101111001", alu.increment_16_bit(a))

        a = "0111111111111111"
        self.assertEqual("1000000000000000", alu.increment_16_bit(a))

    def test_alu_16_bit (self):
        a = "1010101111011111"
        b = "1101011000010011"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_16_bit_operation(a, b, alu.ZERO))

        a = "1001001010010000"
        b = "1110011101110101"
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_16_bit_operation(a, b, alu.ONE))

        a = "1000111101001011"
        b = "0000101110011101"
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_16_bit_operation(a, b, alu.NEGATIVE_ONE))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([a, "0", "0"], alu.alu_16_bit_operation(a, b, alu.X))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([b, "0", "0"], alu.alu_16_bit_operation(a, b, alu.Y))

        x = "1000010000111100"
        y = "1010011010111110"
        self.assertEqual(["0111101111000011", "0", "0"], alu.alu_16_bit_operation(x, y, alu.BITWISE_NEGATION_X))
        self.assertEqual(["0101100101000001", "0", "0"], alu.alu_16_bit_operation(x, y, alu.BITWISE_NEGATION_Y))

        x = "0011100010110001"
        y = "1111010001001100"
        self.assertEqual(["1100011101001111", "0", "1"], alu.alu_16_bit_operation(x, y, alu.NEGATIVE_X))
        self.assertEqual(["0000101110110100", "0", "0"], alu.alu_16_bit_operation(x, y, alu.NEGATIVE_Y))

        x = "1000111101010111"
        y = "0100001001011101"
        self.assertEqual(["1000111101011000", "0", "1"], alu.alu_16_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0100001001011110", "0", "0"], alu.alu_16_bit_operation(x, y, alu.INCREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_16_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_16_bit_operation(x, y, alu.INCREMENT_Y))

        x = "0101111100101101"
        y = "0111110011110000"
        self.assertEqual(["0101111100101100", "0", "0"], alu.alu_16_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["0111110011101111", "0", "0"], alu.alu_16_bit_operation(x, y, alu.DECREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["1111111111111110", "0", "1"], alu.alu_16_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_16_bit_operation(x, y, alu.DECREMENT_Y))

        x = "0000000000000000"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_16_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0100011111111010", "0", "0"], alu.alu_16_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0000000011111100", "0", "0"], alu.alu_16_bit_operation(x, y, alu.SUB_X_Y))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["1111111100000100", "0", "1"], alu.alu_16_bit_operation(x, y, alu.SUB_Y_X))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1001001010010100", "0", "1"], alu.alu_16_bit_operation(x, y, alu.BITWISE_AND))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1101001110111111", "0", "1"], alu.alu_16_bit_operation(x, y, alu.BITWISE_OR))









if __name__ == '__main__':
    unittest.main()