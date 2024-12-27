import unittest
from sequential_logic import sequential as seq
from random_access_memory import Ram_n

class Test(unittest.TestCase):


    def test_bit(self):
        s = seq()
        self.assertEqual(0, s.bit(0, 0))
        self.assertEqual(0, s.bit(1, 0))
        self.assertEqual(1, s.bit(1, 1))
        self.assertEqual(1, s.bit(0, 0))
        self.assertEqual(1, s.bit(1, 0))
        self.assertEqual(0, s.bit(0, 1))

    def test_n_bit_register(self):
        s = seq()
        self.assertEqual(0, s.register_16_bit(0, 0))
        self.assertEqual(0, s.register_16_bit(1, 0))
        self.assertEqual(1, s.register_16_bit(1, 1))
        self.assertEqual(1, s.register_16_bit(0, 0))
        self.assertEqual(1, s.register_16_bit(1, 0))
        self.assertEqual(0, s.register_16_bit(0, 1))

        self.assertEqual(0b0000, s.register_16_bit(0b0000, 1))
        self.assertEqual(0b0000, s.register_16_bit(0b1010, 0))

        self.assertEqual(0b0000000000000000, s.register_16_bit(0b0000000000000000, 1))
        self.assertEqual(0b0100001000000000, s.register_16_bit(0b0100001000000000, 1))
        self.assertEqual(0b0100001000000000, s.register_16_bit(0b0100000000000000, 0))
        self.assertEqual(0b0100000000000000, s.register_16_bit(0b0100000000000000, 1))

    def test_ram_n(self):
        ram = Ram_n(8, 4)

        self.assertEqual([0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000 ], ram.get_list_of_all_register_values())
        self.assertEqual(0000, ram.do_operation(0b1111, 000, 0))
        self.assertEqual([0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000 ], ram.get_list_of_all_register_values())
        self.assertEqual(0b1111, ram.do_operation(0b1111, 000, 1))
        self.assertEqual([0b1111, 0000, 0000, 0000, 0000, 0000, 0000, 0000 ], ram.get_list_of_all_register_values())
        self.assertEqual(0b1010, ram.do_operation(0b1010, 0b100, 1))
        self.assertEqual([0b1111, 0000, 0000, 0000, 0b1010, 0000, 0000, 0000 ], ram.get_list_of_all_register_values())

        ram = Ram_n(16, 8)
        self.assertEqual([  00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000  ], ram.get_list_of_all_register_values())
        self.assertEqual(0b00100110, ram.do_operation(0b00100110, 0b1000, 1))
        self.assertEqual([  00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b00100110, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000  ], ram.get_list_of_all_register_values())

        self.assertEqual(0b01111111, ram.do_operation(0b01111111, 0b1000, 1))
        self.assertEqual([  00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000  ], ram.get_list_of_all_register_values())

        self.assertEqual(0b11001110, ram.do_operation(0b11001110, 0b1111, 1))
        self.assertEqual([  00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 0b11001110  ], ram.get_list_of_all_register_values())

        self.assertEqual(0b10101111, ram.do_operation(0b10101111, 0000, 1))
        self.assertEqual([  0b10101111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 0b11001110  ], ram.get_list_of_all_register_values())

        self.assertEqual(0b00001110, ram.do_operation(0b00001110, 0b1011, 1))
        self.assertEqual([  0b10101111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 0b00001110, 00000000, 00000000, 00000000, 0b11001110  ], ram.get_list_of_all_register_values())

        self.assertEqual(0b01001110, ram.do_operation(0b01001110, 0b1110, 1))
        self.assertEqual([  0b10101111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 0b00001110, 00000000, 00000000, 0b01001110, 0b11001110  ], ram.get_list_of_all_register_values())


        # Reading 
        self.assertEqual(0b10101111, ram.do_operation(00000000, 0000, 0))
        self.assertEqual(00000000, ram.do_operation(00000000, 0b0101, 0))
        self.assertEqual(0b01111111, ram.do_operation(00000000, 0b1000, 0))
        self.assertEqual(0b00001110, ram.do_operation(00000000, 0b1011, 0))
        self.assertEqual(0b11001110, ram.do_operation(00000000, 0b1111, 0))
        self.assertEqual(0b01001110, ram.do_operation(00000000, 0b1110, 0))

        self.assertEqual([  0b10101111, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
                            0b01111111, 00000000, 00000000, 0b00001110, 00000000, 00000000, 0b01001110, 0b11001110  ], ram.get_list_of_all_register_values())

    def test_PC_counter(self):
        s = seq()

        input, inc, load, reset = 1, 0, 0, 0
        self.assertEqual(0, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 1, 0, 0, 0
        self.assertEqual(0, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 1, 1, 0, 0
        self.assertEqual(1, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 1, 0, 0, 0
        self.assertEqual(1, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 1, 1, 0, 0
        self.assertEqual(2, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 1, 0, 0, 0
        self.assertEqual(2, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001010, 0, 1, 0
        self.assertEqual(0b1000100110001010, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001010, 1, 0, 0
        self.assertEqual(0b1000100110001011, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001011, 0, 0, 0
        self.assertEqual(0b1000100110001011, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001011, 0, 0, 1
        self.assertEqual(0b0000000000000000, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001011, 1, 0, 0
        self.assertEqual(0b0000000000000001, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1000100110001011, 0, 0, 0
        self.assertEqual(0b0000000000000001, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1111111111111111, 0, 1, 0
        self.assertEqual(0b1111111111111111, s.PC_counter_16_bit(input, inc, load, reset))

        input, inc, load, reset = 0b1111111111111111, 1, 0, 0
        self.assertEqual(0b0000000000000000, s.PC_counter_16_bit(input, inc, load, reset))






        












if __name__ == '__main__':
    unittest.main()