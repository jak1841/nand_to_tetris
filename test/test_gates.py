from logic_gates import gate as g
import unittest

gate = g()

class Test(unittest.TestCase):

    def test_nand(self):
        self.assertEqual(0, gate.nand(1, 1) & 0x1)
        self.assertEqual(1, gate.nand(1, 0) & 0x1)
        self.assertEqual(1, gate.nand(0, 1) & 0x1)
        self.assertEqual(1, gate.nand(0, 0) & 0x1)

    def test_not(self):
        self.assertEqual(0, gate.not_(1) & 0x1)
        self.assertEqual(1, gate.not_(0) & 0x1)

    def test_and(self):
        self.assertEqual(1, gate.and_(1, 1) & 0x1)
        self.assertEqual(0, gate.and_(1, 0) & 0x1)
        self.assertEqual(0, gate.and_(0, 1) & 0x1)
        self.assertEqual(0, gate.and_(0, 0) & 0x1)

    def test_or(self):
        self.assertEqual(1, gate.or_(1, 1) & 0x1)
        self.assertEqual(1, gate.or_(1, 0) & 0x1)
        self.assertEqual(1, gate.or_(0, 1) & 0x1)
        self.assertEqual(0, gate.or_(0, 0) & 0x1)

    def test_xor(self):
        self.assertEqual(0, gate.xor(1, 1) & 0x1)
        self.assertEqual(1, gate.xor(1, 0) & 0x1)
        self.assertEqual(1, gate.xor(0, 1) & 0x1)
        self.assertEqual(0, gate.xor(0, 0) & 0x1)

    def test_multiplexor(self):
        self.assertEqual(0, gate.multiplexor(0, 0, 0) & 0x1)
        self.assertEqual(0, gate.multiplexor(0, 1, 0) & 0x1)
        self.assertEqual(1, gate.multiplexor(1, 0, 0) & 0x1)
        self.assertEqual(1, gate.multiplexor(1, 1, 0) & 0x1)
        self.assertEqual(0, gate.multiplexor(0, 0, 1) & 0x1)
        self.assertEqual(1, gate.multiplexor(0, 1, 1) & 0x1)
        self.assertEqual(0, gate.multiplexor(1, 0, 1) & 0x1)
        self.assertEqual(1, gate.multiplexor(1, 1, 1) & 0x1)

    def test_demultiplexor(self):
        self.assertEqual([0, 1], gate.demultiplexor(1, 1))
        self.assertEqual([1, 0], gate.demultiplexor(1, 0))
        self.assertEqual([0, 0], gate.demultiplexor(0, 1))
        self.assertEqual([0, 0], gate.demultiplexor(0, 0))

    def test_n_bit_multiplexor(self):
        a = 0
        b = 1
        self.assertEqual(0, gate.n_bit_multipexor(a, b, 0))
        self.assertEqual(1, gate.n_bit_multipexor(a, b, 1))

        a = 0xAB
        b = 0xFE
        self.assertEqual(a, gate.n_bit_multipexor(a, b, 0))
        self.assertEqual(b, gate.n_bit_multipexor(a, b, 1))

        a = 0x0860
        b = 0xFEFE
        self.assertEqual(0x0860, gate.n_bit_multipexor(a, b, 0))
        self.assertEqual(0xFEFE, gate.n_bit_multipexor(a, b, 1))

    def test_n_bit_demultiplexor(self):
        input = 1
        self.assertEqual([1, 0], gate.n_bit_demultplexor(input, 0))
        self.assertEqual([0, 1], gate.n_bit_demultplexor(input, 1))

        input = 10101010
        self.assertEqual([10101010, 00000000], gate.n_bit_demultplexor(input, 0))
        self.assertEqual([00000000, 10101010], gate.n_bit_demultplexor(input, 1))

        input = 1111000011110001
        self.assertEqual([1111000011110001, 0000000000000000], gate.n_bit_demultplexor(input, 0))
        self.assertEqual([0000000000000000, 1111000011110001], gate.n_bit_demultplexor(input, 1))

    def test_n_bit_xor (self):
        a = 0
        b = 1
        self.assertEqual(1, gate.n_bit_xor(a, b))

        a = 0
        b = 0
        self.assertEqual(0, gate.n_bit_xor(a, b))

        a = 1
        b = 0
        self.assertEqual(1, gate.n_bit_xor(a, b))

        a = 1
        b = 1
        self.assertEqual(0, gate.n_bit_xor(a, b))

        a = 0x74
        b = 0x8F
        self.assertEqual(0xFB, gate.n_bit_xor(a, b))

        a = 0xB95E
        b = 0xF029
        self.assertEqual(0x4977, gate.n_bit_xor(a, b))
        
    def test_n_bit_or(self):
        a = 0
        b = 1
        self.assertEqual(1, gate.n_bit_or(a, b))

        a = 0
        b = 0
        self.assertEqual(0, gate.n_bit_or(a, b))

        a = 1
        b = 0
        self.assertEqual(1, gate.n_bit_or(a, b))

        a = 1
        b = 1
        self.assertEqual(1, gate.n_bit_or(a, b))

        a = 0x73
        b = 0x5D 
        self.assertEqual(0x7F, gate.n_bit_or(a, b))

        a = 0x0C52
        b = 0xCA58
        self.assertEqual(0xCE5A, gate.n_bit_or(a, b))
        
    def test_n_bit_and(self):
        a = 0
        b = 1
        self.assertEqual(0, gate.n_bit_and(a, b))

        a = 0
        b = 0
        self.assertEqual(0, gate.n_bit_and(a, b))

        a = 1
        b = 0
        self.assertEqual(0, gate.n_bit_and(a, b))

        a = 1
        b = 1
        self.assertEqual(1, gate.n_bit_and(a, b))

        a = 0x73
        b = 0x5D
        self.assertEqual(0x51, gate.n_bit_and(a, b))

        a = 0x0C52 
        b = 0xCA58
        self.assertEqual(0x0850, gate.n_bit_and(a, b))

    def test_n_bit_not(self):
        a = 0
        self.assertEqual(-1, gate.n_bit_not(a))

        a = 1
        self.assertEqual(-2, gate.n_bit_not(a))

        a = 0xB5F97B29
        self.assertEqual(0x4A0684D6, gate.n_bit_not(a) & 0xFFFFFFFF)

        a = 0x08
        self.assertEqual(-9, gate.n_bit_not(a))

        a = 0xF2EA
        self.assertEqual(0x0D15, gate.n_bit_not(a) & 0xFFFF)

    def test_n_bit_nand(self):
        a = 0
        b = 1
        self.assertEqual(1, gate.n_bit_nand(a, b) & 0x1)

        a = 0
        b = 0
        self.assertEqual(1, gate.n_bit_nand(a, b) & 0x1)

        a = 1
        b = 0
        self.assertEqual(1, gate.n_bit_nand(a, b) & 0x1)

        a = 1
        b = 1
        self.assertEqual(0, gate.n_bit_nand(a, b) & 0x1)

        a = 0x1F04
        b = 0x0549
        self.assertEqual(0xFAFF, gate.n_bit_nand(a, b) & 0xFFFF)

        a = 0x9F
        b = 0x64
        self.assertEqual(0xFB, gate.n_bit_nand(a, b) & 0xFF)

        a = 0x1F58A8FF
        b = 0x0C8C3D24
        self.assertEqual(0xF3F7D7DB, gate.n_bit_nand(a, b) & 0xFFFFFFFF)

    def test_n_bit_all_zeros(self):
        self.assertEqual(1, gate.n_bit_all_zeros(0))
        self.assertEqual(0, gate.n_bit_all_zeros(1))

        self.assertEqual(1, gate.n_bit_all_zeros(0x0000))
        self.assertEqual(0, gate.n_bit_all_zeros(0x10000) & 0xFFFF)
        self.assertEqual(0, gate.n_bit_all_zeros(0x00001))

        self.assertEqual(1, gate.n_bit_all_zeros(0x00))
        self.assertEqual(0, gate.n_bit_all_zeros(0x1AA))
        self.assertEqual(0, gate.n_bit_all_zeros(0x1FF))

    def test_n_bit_4_way_multiplexor(self):
        a = 0x0
        b = 0xA
        c = 0x5 
        d = 0xF
        self.assertEqual(a, gate.n_bit_4_way_multiplexor(a, b, c, d, 0))
        self.assertEqual(b, gate.n_bit_4_way_multiplexor(a, b, c, d, 1))
        self.assertEqual(c, gate.n_bit_4_way_multiplexor(a, b, c, d, 2))
        self.assertEqual(d, gate.n_bit_4_way_multiplexor(a, b, c, d, 3))



        a = 0x3919821
        b = 0x8193821 
        c = 0x8315555
        d = 0x9238210
        self.assertEqual(a, gate.n_bit_4_way_multiplexor(a, b, c, d, 0))
        self.assertEqual(b, gate.n_bit_4_way_multiplexor(a, b, c, d, 1))
        self.assertEqual(c, gate.n_bit_4_way_multiplexor(a, b, c, d, 2))
        self.assertEqual(d, gate.n_bit_4_way_multiplexor(a, b, c, d, 3))


        a = 0x0000550
        b = 0x0400500
        c = 0x0000500
        d = 0x3249223
        self.assertEqual(a, gate.n_bit_4_way_multiplexor(a, b, c, d, 0))
        self.assertEqual(b, gate.n_bit_4_way_multiplexor(a, b, c, d, 1))
        self.assertEqual(c, gate.n_bit_4_way_multiplexor(a, b, c, d, 2))
        self.assertEqual(d, gate.n_bit_4_way_multiplexor(a, b, c, d, 3))



    # Need to fix I am so furstrated
"""
    def test_n_bit_n_way_multiplexor(self):
        list_binary_number = [0x0, 0xA, 0x5, 0xF]
        self.assertEqual(0x0, gate.n_bit_n_way_multiplexor(list_binary_number,  0))
        self.assertEqual(0xA, gate.n_bit_n_way_multiplexor(list_binary_number, 1))
        self.assertEqual(0x5, gate.n_bit_n_way_multiplexor(list_binary_number, 2))
        self.assertEqual(0xF, gate.n_bit_n_way_multiplexor(list_binary_number, 3))

        list_binary_number = [0x43433232, 0x5555555, 0x99999233, 0x99218008]
        self.assertEqual(0x43433232, gate.n_bit_n_way_multiplexor(list_binary_number,  0))
        self.assertEqual(0x5555555, gate.n_bit_n_way_multiplexor(list_binary_number, 1))
        self.assertEqual(0x99999233, gate.n_bit_n_way_multiplexor(list_binary_number, 2))
        self.assertEqual(0x99218008, gate.n_bit_n_way_multiplexor(list_binary_number, 3))


        list_binary_number = [0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22]
        self.assertEqual(list_binary_number[0], gate.n_bit_n_way_multiplexor(list_binary_number, 0x0))
        self.assertEqual(list_binary_number[1], gate.n_bit_n_way_multiplexor(list_binary_number, 0x1))
        self.assertEqual(list_binary_number[2], gate.n_bit_n_way_multiplexor(list_binary_number, 0x2))
        self.assertEqual(list_binary_number[3], gate.n_bit_n_way_multiplexor(list_binary_number, 0x3))
        self.assertEqual(list_binary_number[4], gate.n_bit_n_way_multiplexor(list_binary_number, 0x4))
        self.assertEqual(list_binary_number[5], gate.n_bit_n_way_multiplexor(list_binary_number, 0x5))
        self.assertEqual(list_binary_number[6], gate.n_bit_n_way_multiplexor(list_binary_number, 0x6))
        self.assertEqual(list_binary_number[7], gate.n_bit_n_way_multiplexor(list_binary_number, 0x7))

    def test_n_bit_n_way_demultiplexor(self):
        input = "1"
        self.assertEqual(["1", "0"], gate.n_bit_n_way_demultiplexor(input, "0"))
        self.assertEqual(["0", "1"], gate.n_bit_n_way_demultiplexor(input, "1"))

        input = "1001"
        self.assertEqual(["1001", "0000", "0000", "0000"], gate.n_bit_n_way_demultiplexor(input, "00"))
        self.assertEqual(["0000", "1001", "0000", "0000"], gate.n_bit_n_way_demultiplexor(input, "01"))
        self.assertEqual(["0000", "0000", "1001", "0000"], gate.n_bit_n_way_demultiplexor(input, "10"))
        self.assertEqual(["0000", "0000", "0000", "1001"], gate.n_bit_n_way_demultiplexor(input, "11"))

        input = "01011011"
        self.assertEqual(["01011011", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "000"))
        self.assertEqual(["00000000", "01011011", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "001"))
        self.assertEqual(["00000000", "00000000", "01011011", "00000000", "00000000", "00000000", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "010"))
        self.assertEqual(["00000000", "00000000", "00000000", "01011011", "00000000", "00000000", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "011"))
        self.assertEqual(["00000000", "00000000", "00000000", "00000000", "01011011", "00000000", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "100"))
        self.assertEqual(["00000000", "00000000", "00000000", "00000000", "00000000", "01011011", "00000000", "00000000"], gate.n_bit_n_way_demultiplexor(input, "101"))
        self.assertEqual(["00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "01011011", "00000000"], gate.n_bit_n_way_demultiplexor(input, "110"))
        self.assertEqual(["00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "01011011"], gate.n_bit_n_way_demultiplexor(input, "111"))
"""
if __name__ == '__main__':
    unittest.main()
