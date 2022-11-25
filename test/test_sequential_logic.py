import unittest
import sys

# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')
from sequential_logic import seq as s


class Test(unittest.TestCase):
    def test_SR_AND_OR_latch(self):
        seq = s("0")
        self.assertEqual("0", seq.SR_AND_OR_latch("0", "0"))
        seq = s("1")
        self.assertEqual("1", seq.SR_AND_OR_latch("0", "0"))

        seq = s("0")
        self.assertEqual("1", seq.SR_AND_OR_latch("1", "0"))
        seq = s("1")
        self.assertEqual("1", seq.SR_AND_OR_latch("1", "0"))

        seq = s("0")
        self.assertEqual("0", seq.SR_AND_OR_latch("0", "1"))
        seq = s("1")
        self.assertEqual("0", seq.SR_AND_OR_latch("0", "1"))

        seq = s("0")
        self.assertEqual("0", seq.SR_AND_OR_latch("1", "1"))
        seq = s("1")
        self.assertEqual("0", seq.SR_AND_OR_latch("1", "1"))

    def test_d_latch(self):
        seq = s("0")
        self.assertEqual("0", seq.d_latch("0", "0"))

        seq = s("0")
        self.assertEqual("0", seq.d_latch("1", "0"))

        seq = s("0")
        self.assertEqual("1", seq.d_latch("1", "1"))

        seq = s("0")
        self.assertEqual("0", seq.d_latch("0", "1"))

        seq = s("1")
        self.assertEqual("1", seq.d_latch("0", "0"))

        seq = s("1")
        self.assertEqual("1", seq.d_latch("1", "0"))

        seq = s("1")
        self.assertEqual("1", seq.d_latch("1", "1"))

        seq = s("1")
        self.assertEqual("0", seq.d_latch("0", "1"))






if __name__ == '__main__':
    unittest.main()