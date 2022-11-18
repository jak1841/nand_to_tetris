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






if __name__ == '__main__':
    unittest.main()