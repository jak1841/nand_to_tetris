import unittest
import sys

# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')
from logic_gates import sequential as seq

class Test(unittest.TestCase):


    def test_bit(self):
        s = seq()
        self.assertEqual("0", s.bit("0", "0"))

        self.assertEqual("0", s.bit("1", "0"))

        self.assertEqual("1", s.bit("1", "1"))

        self.assertEqual("1", s.bit("0", "0"))

        self.assertEqual("1", s.bit("1", "0"))

        self.assertEqual("0", s.bit("0", "1"))





        pass

    def test_n_bit_register(self):
        s = seq()
        self.assertEqual("0", s.register_n_bit("0", "0"))
        self.assertEqual("0", s.register_n_bit("1", "0"))
        self.assertEqual("1", s.register_n_bit("1", "1"))
        self.assertEqual("1", s.register_n_bit("0", "0"))
        self.assertEqual("1", s.register_n_bit("1", "0"))
        self.assertEqual("0", s.register_n_bit("0", "1"))

        self.assertEqual("0000", s.register_n_bit("0000", "1"))
        self.assertEqual("0000", s.register_n_bit("1010", "0"))

        self.assertEqual("0000000000000000", s.register_n_bit("0000000000000000", "1"))
        self.assertEqual("0100001000000000", s.register_n_bit("0100001000000000", "1"))
        self.assertEqual("0100001000000000", s.register_n_bit("0100000000000000", "0"))
        self.assertEqual("0100000000000000", s.register_n_bit("0100000000000000", "1"))













if __name__ == '__main__':
    unittest.main()