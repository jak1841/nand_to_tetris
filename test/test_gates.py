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
        self.assertEqual("01", gate.demultiplexor("1", "1"))
        self.assertEqual("10", gate.demultiplexor("1", "0"))
        self.assertEqual("00", gate.demultiplexor("0", "1"))
        self.assertEqual("00", gate.demultiplexor("0", "0"))

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


if __name__ == '__main__':
    unittest.main()
