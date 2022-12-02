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
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(a, b, alu.ZERO))

        a = "1001001010010000"
        b = "1110011101110101"
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_n_bit_operation(a, b, alu.ONE))

        a = "1000111101001011"
        b = "0000101110011101"
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_n_bit_operation(a, b, alu.NEGATIVE_ONE))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([a, "0", "0"], alu.alu_n_bit_operation(a, b, alu.X))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([b, "0", "0"], alu.alu_n_bit_operation(a, b, alu.Y))

        x = "1000010000111100"
        y = "1010011010111110"
        self.assertEqual(["0111101111000011", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_X))
        self.assertEqual(["0101100101000001", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_Y))

        x = "0011100010110001"
        y = "1111010001001100"
        self.assertEqual(["1100011101001111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_X))
        self.assertEqual(["0000101110110100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_Y))

        x = "1000111101010111"
        y = "0100001001011101"
        self.assertEqual(["1000111101011000", "0", "1"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0100001001011110", "0", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = "0101111100101101"
        y = "0111110011110000"
        self.assertEqual(["0101111100101100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["0111110011101111", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["1111111111111110", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = "0000000000000000"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0100011111111010", "0", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0000000011111100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.SUB_X_Y))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["1111111100000100", "0", "1"], alu.alu_n_bit_operation(x, y, alu.SUB_Y_X))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1001001010010100", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_AND))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1101001110111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_OR))

    def test_adder_n_bit (self):
        a = "0000000000000000"
        b = "0000000000000001"
        self.assertEqual("0000000000000001", alu.adder_n_bit(a, b))

        a = "1111111111111111"
        b = "0000000000000001"
        self.assertEqual("0000000000000000", alu.adder_n_bit(a, b))

        a = "1111111111111111"
        b = "0000000000000001"
        self.assertEqual("0000000000000000", alu.adder_n_bit(a, b))

        a = "1010101010101010"
        b = "0101010101010101"
        self.assertEqual("1111111111111111", alu.adder_n_bit(a, b))


        a = "0101010101111000"
        b = "1100110000000000"
        self.assertEqual("0010000101111000", alu.adder_n_bit(a, b))

        a = "1010010101010101"
        b = "1111111100001111"
        self.assertEqual("1010010001100100", alu.adder_n_bit(a, b))

        a = "00011111"
        b = "01010001"
        self.assertEqual("01110000", alu.adder_n_bit(a, b))

        a = "11100110"
        b = "10111110"
        self.assertEqual("10100100", alu.adder_n_bit(a, b))

        a = "01110011111001100001001101001000"
        b = "11000100110111010000100100100011"
        self.assertEqual("00111000110000110001110001101011", alu.adder_n_bit(a, b))

    def test_incrementer_n_bit (self):
        a = "1010101101101011"
        self.assertEqual("1010101101101100", alu.increment_n_bit(a))

        a = "1110010101011111"
        self.assertEqual("1110010101100000", alu.increment_n_bit(a))

        a = "1111111111111111"
        self.assertEqual("0000000000000000", alu.increment_n_bit(a))

        a = "0000000000000000"
        self.assertEqual("0000000000000001", alu.increment_n_bit(a))

        a = "1011101010110010"
        self.assertEqual("1011101010110011", alu.increment_n_bit(a))

        a = "1111111101111000"
        self.assertEqual("1111111101111001", alu.increment_n_bit(a))

        a = "0111111111111111"
        self.assertEqual("1000000000000000", alu.increment_n_bit(a))

        a = "10011100010110011001111000101100"
        self.assertEqual("10011100010110011001111000101101", alu.increment_n_bit(a))

        a = "10011100010110011001111000101100"
        self.assertEqual("10011100010110011001111000101101", alu.increment_n_bit(a))

        a = "11110011"
        self.assertEqual("11110100", alu.increment_n_bit(a))

        a = "0011000000000000101110111111110000101001101100100101100000110111"
        self.assertEqual("0011000000000000101110111111110000101001101100100101100000111000", alu.increment_n_bit(a))

    def test_alu_n_bit (self):
        a = "1010101111011111"
        b = "1101011000010011"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(a, b, alu.ZERO))

        a = "1001001010010000"
        b = "1110011101110101"
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_n_bit_operation(a, b, alu.ONE))

        a = "1000111101001011"
        b = "0000101110011101"
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_n_bit_operation(a, b, alu.NEGATIVE_ONE))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([a, "0", "0"], alu.alu_n_bit_operation(a, b, alu.X))

        a = "0011001011001111"
        b = "0001111101010010"
        self.assertEqual([b, "0", "0"], alu.alu_n_bit_operation(a, b, alu.Y))

        x = "1000010000111100"
        y = "1010011010111110"
        self.assertEqual(["0111101111000011", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_X))
        self.assertEqual(["0101100101000001", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_Y))

        x = "0011100010110001"
        y = "1111010001001100"
        self.assertEqual(["1100011101001111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_X))
        self.assertEqual(["0000101110110100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_Y))

        x = "1000111101010111"
        y = "0100001001011101"
        self.assertEqual(["1000111101011000", "0", "1"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0100001001011110", "0", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["0000000000000001", "0", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = "0101111100101101"
        y = "0111110011110000"
        self.assertEqual(["0101111100101100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["0111110011101111", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = "1111111111111111"
        y = "0000000000000000"
        self.assertEqual(["1111111111111110", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["1111111111111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = "0000000000000000"
        y = "0000000000000000"
        self.assertEqual(["0000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0100011111111010", "0", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["0000000011111100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.SUB_X_Y))

        x = "1010010001111011"
        y = "1010001101111111"
        self.assertEqual(["1111111100000100", "0", "1"], alu.alu_n_bit_operation(x, y, alu.SUB_Y_X))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1001001010010100", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_AND))

        x = "1101001110010111"
        y = "1001001010111100"
        self.assertEqual(["1101001110111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_OR))

        """
            32 bit testing lolz
        
        """

        a = "10101011110111111010101111011111"
        b = "11010110000100111010101111011111"
        self.assertEqual(["00000000000000000000000000000000", "1", "0"], alu.alu_n_bit_operation(a, b, alu.ZERO))

        a = "10010010100100001001001010010000"
        b = "11100111011101011001001010010000"
        self.assertEqual(["00000000000000000000000000000001", "0", "0"], alu.alu_n_bit_operation(a, b, alu.ONE))

        a = "10001111010010111000111101001011"
        b = "00001011100111011000111101001011"
        self.assertEqual(["11111111111111111111111111111111", "0", "1"], alu.alu_n_bit_operation(a, b, alu.NEGATIVE_ONE))

        a = "00110010110011110011001011001111"
        b = "00011111010100100011001011001111"
        self.assertEqual([a, "0", "0"], alu.alu_n_bit_operation(a, b, alu.X))

        a = "00110010110011110011001011001111"
        b = "00011111010100100011001011001111"
        self.assertEqual([b, "0", "0"], alu.alu_n_bit_operation(a, b, alu.Y))

        x = "10000100001111001000010000111100"
        y = "10100110101111101000010000111100"
        self.assertEqual(["01111011110000110111101111000011", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_X))
        self.assertEqual(["01011001010000010111101111000011", "0", "0"], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_Y))

        x = "00111000101100010011100010110001"
        y = "11110100010011000011100010110001"
        self.assertEqual(["11000111010011101100011101001111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_X))
        self.assertEqual(["00001011101100111100011101001111", "0", "0"], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_Y))

        x = "10001111010101111000111101010111"
        y = "01000010010111010100001001011101"
        self.assertEqual(["10001111010101111000111101011000", "0", "1"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["01000010010111010100001001011110", "0", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = "11111111111111111111111111111111"
        y = "01111111111111111111111111111111"
        self.assertEqual(["00000000000000000000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual(["10000000000000000000000000000000", "0", "1"], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))



        x = "01011111001011010101111100101101"
        y = "01111100111100000111110011110000"
        self.assertEqual(["01011111001011010101111100101100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["01111100111100000111110011101111", "0", "0"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = "11111111111111111111111111111111"
        y = "00000000000000000000000000000000"
        self.assertEqual(["11111111111111111111111111111110", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual(["11111111111111111111111111111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))



        x = "00000000000000000000000000000000"
        y = "00000000000000000000000000000000"
        self.assertEqual(["00000000000000000000000000000000", "1", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "10100100011110111010010001111011"
        y = "10100011011111111010001101111111"
        self.assertEqual(["01000111111110110100011111111010", "0", "0"], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = "10100100011110111010010001111011"
        y = "10100011011111111010001101111111"
        self.assertEqual(["00000000111111000000000011111100", "0", "0"], alu.alu_n_bit_operation(x, y, alu.SUB_X_Y))

        x = "10100100011110111010010001111011"
        y = "10100011011111111010010001111011"
        self.assertEqual(["11111111000001000000000000000000", "0", "1"], alu.alu_n_bit_operation(x, y, alu.SUB_Y_X))

        x = "11010011100101111101001110010111"
        y = "10010010101111001001001010111100"
        self.assertEqual(["10010010100101001001001010010100", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_AND))

        x = "11010011100101111101001110010111"
        y = "10010010101111001001001010111100"
        self.assertEqual(["11010011101111111101001110111111", "0", "1"], alu.alu_n_bit_operation(x, y, alu.BITWISE_OR))


if __name__ == '__main__':
    unittest.main()