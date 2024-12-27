import unittest
from arithemtic_logic_unit import alu as a
alu = a()

class Test(unittest.TestCase):
    def test_half_adder(self):
        self.assertEqual((0, 0), alu.half_adder(0, 0))
        self.assertEqual((0, 1), alu.half_adder(1, 0))
        self.assertEqual((0, 1), alu.half_adder(0, 1))
        self.assertEqual((1, 0), alu.half_adder(1, 1))

    def test_full_adder(self):
        self.assertEqual((0, 0), alu.full_adder(0, 0, 0))
        self.assertEqual((0, 1), alu.full_adder(1, 0, 0))
        self.assertEqual((0, 1), alu.full_adder(0, 1, 0))
        self.assertEqual((0, 1), alu.full_adder(0, 0, 1))
        self.assertEqual((1, 0), alu.full_adder(1, 1, 0))
        self.assertEqual((1, 0), alu.full_adder(1, 0, 1))
        self.assertEqual((1, 0), alu.full_adder(0, 1, 1))
        self.assertEqual((1, 1), alu.full_adder(1, 1, 1))

    def test_adder_16_bit (self):
        a = 0x0000
        b = 0x0001
        self.assertEqual(0x0001, alu.adder_16_bit(a, b))

        a = 0xFFFF
        b = 0x0001
        self.assertEqual(0x0000, alu.adder_16_bit(a, b))

        a = 0xFFFF
        b = 0x0001
        self.assertEqual(0x0000, alu.adder_16_bit(a, b))

        a = 0xAAAA
        b = 0x5555
        self.assertEqual(0xFFFF, alu.adder_16_bit(a, b))


        a = 0x5578
        b = 0xCC00
        self.assertEqual(0x2178, alu.adder_16_bit(a, b))

        a = 0xA555
        b = 0xFF0F
        self.assertEqual(0xA464, alu.adder_16_bit(a, b))
        

    def test_incrementer_16_bit (self):
        a = 0xAB5B
        self.assertEqual(0xAB5C, alu.increment_16_bit(a))

        a = 0xFFFF
        self.assertEqual(0x0000, alu.increment_16_bit(a))

        a = 0x0000
        self.assertEqual(0x0001, alu.increment_16_bit(a))

        a = 0xFF78
        self.assertEqual(0xFF79, alu.increment_16_bit(a))

        a = 0x7FFF
        self.assertEqual(0x8000, alu.increment_16_bit(a))

    def test_alu_16_bit (self):
        a = 0b1010101111011111
        b = 0b1101011000010011
        self.assertEqual([0b0000000000000000, 1, 0], alu.alu_n_bit_operation(a, b, alu.ZERO))

        a = 0b1001001010010000
        b = 0b1110011101110101
        self.assertEqual([0b0000000000000001, 0, 0], alu.alu_n_bit_operation(a, b, alu.ONE))

        a = 0b1000111101001011
        b = 0b0000101110011101
        self.assertEqual([0b1111111111111111, 0, 1], alu.alu_n_bit_operation(a, b, alu.NEGATIVE_ONE))

        a = 0b0011001011001111
        b = 0b0001111101010010
        self.assertEqual([a, 0, 0], alu.alu_n_bit_operation(a, b, alu.X))

        a = 0b0011001011001111
        b = 0b0001111101010010
        self.assertEqual([b, 0, 0], alu.alu_n_bit_operation(a, b, alu.Y))

        x = 0b1000010000111100
        y = 0b1010011010111110
        self.assertEqual([0b0111101111000011, 0, 0], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_X))
        self.assertEqual([0b0101100101000001, 0, 0], alu.alu_n_bit_operation(x, y, alu.BITWISE_NEGATION_Y))

        x = 0b0011100010110001
        y = 0b1111010001001100
        self.assertEqual([0b1100011101001111, 0, 1], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_X))
        self.assertEqual([0b0000101110110100, 0, 0], alu.alu_n_bit_operation(x, y, alu.NEGATIVE_Y))

        x = 0b1000111101010111
        y = 0b0100001001011101
        self.assertEqual([0b1000111101011000, 0, 1], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual([0b0100001001011110, 0, 0], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = 0b1111111111111111
        y = 0b0000000000000000
        self.assertEqual([0b0000000000000000, 1, 0], alu.alu_n_bit_operation(x, y, alu.INCREMENT_X))
        self.assertEqual([0b0000000000000001, 0, 0], alu.alu_n_bit_operation(x, y, alu.INCREMENT_Y))

        x = 0b0101111100101101
        y = 0b0111110011110000
        self.assertEqual([0b0101111100101100, 0, 0], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual([0b0111110011101111, 0, 0], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = 0b1111111111111111
        y = 0b0000000000000000
        self.assertEqual([0b1111111111111110, 0, 1], alu.alu_n_bit_operation(x, y, alu.DECREMENT_X))
        self.assertEqual([0b1111111111111111, 0, 1], alu.alu_n_bit_operation(x, y, alu.DECREMENT_Y))

        x = 0b0000000000000000
        y = 0b0000000000000000
        self.assertEqual([0b0000000000000000, 1, 0], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = 0b1010010001111011
        y = 0b1010001101111111
        self.assertEqual([0b0100011111111010, 0, 0], alu.alu_n_bit_operation(x, y, alu.ADD))

        x = 0b1010010001111011
        y = 0b1010001101111111
        self.assertEqual([0b0000000011111100, 0, 0], alu.alu_n_bit_operation(x, y, alu.SUB_X_Y))

        x = 0b1010010001111011
        y = 0b1010001101111111
        self.assertEqual([0b1111111100000100, 0, 1], alu.alu_n_bit_operation(x, y, alu.SUB_Y_X))

        x = 0b1101001110010111
        y = 0b1001001010111100
        self.assertEqual([0b1001001010010100, 0, 1], alu.alu_n_bit_operation(x, y, alu.BITWISE_AND))

        x = 0b1101001110010111
        y = 0b1001001010111100
        self.assertEqual([0b1101001110111111, 0, 1], alu.alu_n_bit_operation(x, y, alu.BITWISE_OR))

    def test_adder_n_bit (self):
        a = 0b0000000000000000
        b = 0b0000000000000001
        self.assertEqual(0b0000000000000001, alu.adder_n_bit(a, b))

        a = 0b1111111111111111
        b = 0b0000000000000001
        self.assertEqual(0b0000000000000000, alu.adder_n_bit(a, b))

        a = 0b1111111111111111
        b = 0b0000000000000001
        self.assertEqual(0b0000000000000000, alu.adder_n_bit(a, b))

        a = 0b1010101010101010
        b = 0b0101010101010101
        self.assertEqual(0b1111111111111111, alu.adder_n_bit(a, b))


        a = 0b0101010101111000
        b = 0b1100110000000000
        self.assertEqual(0b0010000101111000, alu.adder_n_bit(a, b))

        a = 0b1010010101010101
        b = 0b1111111100001111
        self.assertEqual(0b1010010001100100, alu.adder_n_bit(a, b))

        a = 0b00011111
        b = 0b01010001
        self.assertEqual(0b01110000, alu.adder_n_bit(a, b))

        a = 0b11100110
        b = 0b10111110
        self.assertEqual(0b10100100, alu.adder_n_bit(a, b))

        a = 0b01110011111001100001001101001000
        b = 0b11000100110111010000100100100011
        self.assertEqual(0b00111000110000110001110001101011, alu.adder_n_bit(a, b))

    def test_incrementer_n_bit (self):
        a = 0b1010101101101011
        self.assertEqual(0b1010101101101100, alu.increment_n_bit(a))

        a = 0b1110010101011111
        self.assertEqual(0b1110010101100000, alu.increment_n_bit(a))

        a = 0b1111111111111111
        self.assertEqual(0b0000000000000000, alu.increment_n_bit(a))

        a = 0b0000000000000000
        self.assertEqual(0b0000000000000001, alu.increment_n_bit(a))

        a = 0b1011101010110010
        self.assertEqual(0b1011101010110011, alu.increment_n_bit(a))

        a = 0b1111111101111000
        self.assertEqual(0b1111111101111001, alu.increment_n_bit(a))

        a = 0b0111111111111111
        self.assertEqual(0b0000000000000000, alu.increment_n_bit(a))

        a = 0b10011100010110011001111000101100
        self.assertEqual(0b10011100010110011001111000101101, alu.increment_n_bit(a))

        a = 0b10011100010110011001111000101100
        self.assertEqual(0b10011100010110011001111000101101, alu.increment_n_bit(a))

        a = 0b11110011
        self.assertEqual(0b11110100, alu.increment_n_bit(a))

        a = 0b0011000000000000101110111111110000101001101100100101100000110111
        self.assertEqual(0b0011000000000000101110111111110000101001101100100101100000111000, alu.increment_n_bit(a))

if __name__ == '__main__':
    unittest.main()