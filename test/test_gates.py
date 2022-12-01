import unittest
import sys

# allows use of
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')
from logic_gates import gate as g

gate = g()

class Test(unittest.TestCase):

    def test_nand(self):
        self.assertEqual("0", gate.nand("1", "1"))
        self.assertEqual("1", gate.nand("1", "0"))
        self.assertEqual("1", gate.nand("0", "1"))
        self.assertEqual("1", gate.nand("0", "0"))

    def test_not(self):
        self.assertEqual("0", gate.not_("1"))
        self.assertEqual("1", gate.not_("0"))

    def test_and(self):
        self.assertEqual("1", gate.and_("1", "1"))
        self.assertEqual("0", gate.and_("1", "0"))
        self.assertEqual("0", gate.and_("0", "1"))
        self.assertEqual("0", gate.and_("0", "0"))

    def test_or(self):
        self.assertEqual("1", gate.or_("1", "1"))
        self.assertEqual("1", gate.or_("1", "0"))
        self.assertEqual("1", gate.or_("0", "1"))
        self.assertEqual("0", gate.or_("0", "0"))

    def test_xor(self):
        self.assertEqual("0", gate.xor("1", "1"))
        self.assertEqual("1", gate.xor("1", "0"))
        self.assertEqual("1", gate.xor("0", "1"))
        self.assertEqual("0", gate.xor("0", "0"))

    def test_multiplexor(self):
        self.assertEqual("0", gate.multiplexor("0", "0", "0"))
        self.assertEqual("0", gate.multiplexor("0", "1", "0"))
        self.assertEqual("1", gate.multiplexor("1", "0", "0"))
        self.assertEqual("1", gate.multiplexor("1", "1", "0"))
        self.assertEqual("0", gate.multiplexor("0", "0", "1"))
        self.assertEqual("1", gate.multiplexor("0", "1", "1"))
        self.assertEqual("0", gate.multiplexor("1", "0", "1"))
        self.assertEqual("1", gate.multiplexor("1", "1", "1"))

    def test_demultiplexor(self):
        self.assertEqual(["0", "1"], gate.demultiplexor("1", "1"))
        self.assertEqual(["1", "0"], gate.demultiplexor("1", "0"))
        self.assertEqual(["0", "0"], gate.demultiplexor("0", "1"))
        self.assertEqual(["0", "0"], gate.demultiplexor("0", "0"))

    def test_n_bit_multiplexor(self):
        a = "0"
        b = "1"
        self.assertEqual("0", gate.n_bit_multipexor(a, b, "0"))
        self.assertEqual("1", gate.n_bit_multipexor(a, b, "1"))

        a = "10101011"
        b = "11111110"
        self.assertEqual("10101011", gate.n_bit_multipexor(a, b, "0"))
        self.assertEqual("11111110", gate.n_bit_multipexor(a, b, "1"))

        a = "0000100001100000"
        b = "1111111011111110"
        self.assertEqual("0000100001100000", gate.n_bit_multipexor(a, b, "0"))
        self.assertEqual("1111111011111110", gate.n_bit_multipexor(a, b, "1"))

    def test_n_bit_demultiplexor(self):
        input = "1"
        self.assertEqual(["1", "0"], gate.n_bit_demultplexor(input, "0"))
        self.assertEqual(["0", "1"], gate.n_bit_demultplexor(input, "1"))

        input = "10101010"
        self.assertEqual(["10101010", "00000000"], gate.n_bit_demultplexor(input, "0"))
        self.assertEqual(["00000000", "10101010"], gate.n_bit_demultplexor(input, "1"))

        input = "1111000011110001"
        self.assertEqual(["1111000011110001", "0000000000000000"], gate.n_bit_demultplexor(input, "0"))
        self.assertEqual(["0000000000000000", "1111000011110001"], gate.n_bit_demultplexor(input, "1"))

    def test_n_bit_xor (self):
        a = "0"
        b = "1"
        self.assertEqual("1", gate.n_bit_xor(a, b))

        a = "0"
        b = "0"
        self.assertEqual("0", gate.n_bit_xor(a, b))

        a = "1"
        b = "0"
        self.assertEqual("1", gate.n_bit_xor(a, b))

        a = "1"
        b = "1"
        self.assertEqual("0", gate.n_bit_xor(a, b))

        a = "01110100"
        b = "10001111"
        self.assertEqual("11111011", gate.n_bit_xor(a, b))

        a = "1011100101011110"
        b = "1111000000101001"
        self.assertEqual("0100100101110111", gate.n_bit_xor(a, b))

    def test_n_bit_or(self):
        a = "0"
        b = "1"
        self.assertEqual("1", gate.n_bit_or(a, b))

        a = "0"
        b = "0"
        self.assertEqual("0", gate.n_bit_or(a, b))

        a = "1"
        b = "0"
        self.assertEqual("1", gate.n_bit_or(a, b))

        a = "1"
        b = "1"
        self.assertEqual("1", gate.n_bit_or(a, b))

        a = "01110011"
        b = "01011101"
        self.assertEqual("01111111", gate.n_bit_or(a, b))

        a = "0000110001010010"
        b = "1100101001011000"
        self.assertEqual("1100111001011010", gate.n_bit_or(a, b))

    def test_n_bit_and(self):
        a = "0"
        b = "1"
        self.assertEqual("0", gate.n_bit_and(a, b))

        a = "0"
        b = "0"
        self.assertEqual("0", gate.n_bit_and(a, b))

        a = "1"
        b = "0"
        self.assertEqual("0", gate.n_bit_and(a, b))

        a = "1"
        b = "1"
        self.assertEqual("1", gate.n_bit_and(a, b))

        a = "01110011"
        b = "01011101"
        self.assertEqual("01010001", gate.n_bit_and(a, b))

        a = "0000110001010010"
        b = "1100101001011000"
        self.assertEqual("0000100001010000", gate.n_bit_and(a, b))

    def test_n_bit_not(self):
        a = "0"
        self.assertEqual("1", gate.n_bit_not(a))

        a = "1"
        self.assertEqual("0", gate.n_bit_not(a))

        a = "10110101111110010111101100101001"
        self.assertEqual("01001010000001101000010011010110", gate.n_bit_not(a))

        a = "001000"
        self.assertEqual("110111", gate.n_bit_not(a))

        a = "1111001011101010"
        self.assertEqual("0000110100010101", gate.n_bit_not(a))

    def test_n_bit_nand(self):
        a = "0"
        b = "1"
        self.assertEqual("1", gate.n_bit_nand(a, b))

        a = "0"
        b = "0"
        self.assertEqual("1", gate.n_bit_nand(a, b))

        a = "1"
        b = "0"
        self.assertEqual("1", gate.n_bit_nand(a, b))

        a = "1"
        b = "1"
        self.assertEqual("0", gate.n_bit_nand(a, b))

        a = "0001111100000100"
        b = "0000010101001001"
        self.assertEqual("1111101011111111", gate.n_bit_nand(a, b))

        a = "10011111"
        b = "01100100"
        self.assertEqual("11111011", gate.n_bit_nand(a, b))

        a = "00011111010110001010100011111111"
        b = "00001011100010110011110100100100"
        self.assertEqual("11110100111101111101011111011011", gate.n_bit_nand(a, b))

    def test_n_bit_all_zeros(self):
        self.assertEqual("1", gate.n_bit_all_zeros("0"))
        self.assertEqual("0", gate.n_bit_all_zeros("1"))

        self.assertEqual("1", gate.n_bit_all_zeros("000000000000000000"))
        self.assertEqual("0", gate.n_bit_all_zeros("10000000000000000"))
        self.assertEqual("0", gate.n_bit_all_zeros("000000000000000001"))

        self.assertEqual("1", gate.n_bit_all_zeros("000000"))
        self.assertEqual("0", gate.n_bit_all_zeros("110101010"))
        self.assertEqual("0", gate.n_bit_all_zeros("1111111111111"))

    def test_n_bit_4_way_multiplexor(self):
        a = "0000"
        b = "1010"
        c = "0101"
        d = "1111"
        self.assertEqual("0000", gate.n_bit_4_way_multiplexor(a, b, c, d, "00"))
        self.assertEqual("1010", gate.n_bit_4_way_multiplexor(a, b, c, d, "01"))
        self.assertEqual("0101", gate.n_bit_4_way_multiplexor(a, b, c, d, "10"))
        self.assertEqual("1111", gate.n_bit_4_way_multiplexor(a, b, c, d, "11"))



        a = "00011011011011011000111101001001"
        b = "11011001000111011011101001001100"
        c = "10100100100100100000110001101100"
        d = "10010011111010011101101001110010"
        self.assertEqual(a, gate.n_bit_4_way_multiplexor(a, b, c, d, "00"))
        self.assertEqual(b, gate.n_bit_4_way_multiplexor(a, b, c, d, "01"))
        self.assertEqual(c, gate.n_bit_4_way_multiplexor(a, b, c, d, "10"))
        self.assertEqual(d, gate.n_bit_4_way_multiplexor(a, b, c, d, "11"))


        a = "000100001010000"
        b = "111010111111101"
        c = "110110100001011"
        d = "100110100110010"
        self.assertEqual(a, gate.n_bit_4_way_multiplexor(a, b, c, d, "00"))
        self.assertEqual(b, gate.n_bit_4_way_multiplexor(a, b, c, d, "01"))
        self.assertEqual(c, gate.n_bit_4_way_multiplexor(a, b, c, d, "10"))
        self.assertEqual(d, gate.n_bit_4_way_multiplexor(a, b, c, d, "11"))

    def test_n_bit_n_way_multiplexor(self):
        list_binary_number = ["0000", "1010", "0101", "1111"]
        self.assertEqual("0000", gate.n_bit_n_way_multiplexor(list_binary_number,  "00"))
        self.assertEqual("1010", gate.n_bit_n_way_multiplexor(list_binary_number, "01"))
        self.assertEqual("0101", gate.n_bit_n_way_multiplexor(list_binary_number, "10"))
        self.assertEqual("1111", gate.n_bit_n_way_multiplexor(list_binary_number, "11"))

        list_binary_number = ["00011011011011011000111101001001", "11011001000111011011101001001100", "10100100100100100000110001101100", "10010011111010011101101001110010"]
        self.assertEqual("00011011011011011000111101001001", gate.n_bit_n_way_multiplexor(list_binary_number,  "00"))
        self.assertEqual("11011001000111011011101001001100", gate.n_bit_n_way_multiplexor(list_binary_number, "01"))
        self.assertEqual("10100100100100100000110001101100", gate.n_bit_n_way_multiplexor(list_binary_number, "10"))
        self.assertEqual("10010011111010011101101001110010", gate.n_bit_n_way_multiplexor(list_binary_number, "11"))


        list_binary_number = ["01100111", "01110010", "00001110", "01011010", "01100010", "00101100", "10110011", "01010110"]
        self.assertEqual(list_binary_number[0], gate.n_bit_n_way_multiplexor(list_binary_number,  "000"))
        self.assertEqual(list_binary_number[1], gate.n_bit_n_way_multiplexor(list_binary_number, "001"))
        self.assertEqual(list_binary_number[2], gate.n_bit_n_way_multiplexor(list_binary_number, "010"))
        self.assertEqual(list_binary_number[3], gate.n_bit_n_way_multiplexor(list_binary_number, "011"))
        self.assertEqual(list_binary_number[4], gate.n_bit_n_way_multiplexor(list_binary_number,  "100"))
        self.assertEqual(list_binary_number[5], gate.n_bit_n_way_multiplexor(list_binary_number, "101"))
        self.assertEqual(list_binary_number[6], gate.n_bit_n_way_multiplexor(list_binary_number, "110"))
        self.assertEqual(list_binary_number[7], gate.n_bit_n_way_multiplexor(list_binary_number, "111"))



        


if __name__ == '__main__':
    unittest.main()
