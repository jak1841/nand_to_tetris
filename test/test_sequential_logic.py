import unittest
import sys

# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')
from sequential_logic import sequential as seq
from random_access_memory import Ram_n

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

    def test_ram_n(self):
        ram = Ram_n(8, 4)

        self.assertEqual(["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000" ], ram.get_list_of_all_register_values())
        self.assertEqual("0000", ram.do_operation("1111", "000", "0"))
        self.assertEqual(["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000" ], ram.get_list_of_all_register_values())
        self.assertEqual("1111", ram.do_operation("1111", "000", "1"))
        self.assertEqual(["1111", "0000", "0000", "0000", "0000", "0000", "0000", "0000" ], ram.get_list_of_all_register_values())
        self.assertEqual("1010", ram.do_operation("1010", "100", "1"))
        self.assertEqual(["1111", "0000", "0000", "0000", "1010", "0000", "0000", "0000" ], ram.get_list_of_all_register_values())

        ram = Ram_n(16, 8)
        self.assertEqual([  "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"  ], ram.get_list_of_all_register_values())
        self.assertEqual("00100110", ram.do_operation("00100110", "1000", "1"))
        self.assertEqual([  "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "00100110", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"  ], ram.get_list_of_all_register_values())

        self.assertEqual("01111111", ram.do_operation("01111111", "1000", "1"))
        self.assertEqual([  "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"  ], ram.get_list_of_all_register_values())

        self.assertEqual("11001110", ram.do_operation("11001110", "1111", "1"))
        self.assertEqual([  "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "11001110"  ], ram.get_list_of_all_register_values())

        self.assertEqual("10101111", ram.do_operation("10101111", "0000", "1"))
        self.assertEqual([  "10101111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "11001110"  ], ram.get_list_of_all_register_values())

        self.assertEqual("00001110", ram.do_operation("00001110", "1011", "1"))
        self.assertEqual([  "10101111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00001110", "00000000", "00000000", "00000000", "11001110"  ], ram.get_list_of_all_register_values())

        self.assertEqual("01001110", ram.do_operation("01001110", "1110", "1"))
        self.assertEqual([  "10101111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00001110", "00000000", "00000000", "01001110", "11001110"  ], ram.get_list_of_all_register_values())


        # Reading 
        self.assertEqual("10101111", ram.do_operation("00000000", "0000", "0"))
        self.assertEqual("00000000", ram.do_operation("00000000", "0101", "0"))
        self.assertEqual("01111111", ram.do_operation("00000000", "1000", "0"))
        self.assertEqual("00001110", ram.do_operation("00000000", "1011", "0"))
        self.assertEqual("11001110", ram.do_operation("00000000", "1111", "0"))
        self.assertEqual("01001110", ram.do_operation("00000000", "1110", "0"))

        self.assertEqual([  "10101111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", 
                            "01111111", "00000000", "00000000", "00001110", "00000000", "00000000", "01001110", "11001110"  ], ram.get_list_of_all_register_values())

    def test_PC_counter(self):
        s = seq()

        input, inc, load, reset = "1", "0", "0", "0"
        self.assertEqual("0", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1", "0", "0", "0"
        self.assertEqual("0", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1", "1", "0", "0"
        self.assertEqual("1", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1", "0", "0", "0"
        self.assertEqual("1", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1", "1", "0", "0"
        self.assertEqual("0", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1", "0", "0", "0"
        self.assertEqual("0", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001010", "0", "1", "0"
        self.assertEqual("1000100110001010", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001010", "1", "0", "0"
        self.assertEqual("1000100110001011", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001011", "0", "0", "0"
        self.assertEqual("1000100110001011", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001011", "0", "0", "1"
        self.assertEqual("0000000000000000", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001011", "1", "0", "0"
        self.assertEqual("0000000000000001", s.PC_counter_n_bit(input, inc, load, reset))

        input, inc, load, reset = "1000100110001011", "0", "0", "0"
        self.assertEqual("0000000000000001", s.PC_counter_n_bit(input, inc, load, reset))





        












if __name__ == '__main__':
    unittest.main()