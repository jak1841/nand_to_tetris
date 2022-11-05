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




if __name__ == '__main__':
    unittest.main()
