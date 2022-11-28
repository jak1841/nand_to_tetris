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






if __name__ == '__main__':
    unittest.main()