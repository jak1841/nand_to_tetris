import unittest
import sys


# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')

from hack_assembler import assembler
from hack_computer import computer

class Test(unittest.TestCase):
    def test_fibonacci_program(self):
        program = ['@first_num', 'M=0', '@second_num', 'M=1', '(add_two_previous_store_in_total)', '@total', 'M=0', '@first_num', 'D=M', '@second_num', 'D=D+M', '@total', 'M=D', '(update_previus_two_values)', 
        '@second_num', 'D=M', '@first_num', 'M=D', '@total', 'D=M', '@second_num', 'M=D', '(a_has_first_and_d_has_second)', '@second_num', 'D=M', '@first_num', 'A=M', '@add_two_previous_store_in_total', '0;JMP']
        fibonacci = ['0000000000000010', '0000000000000011', '0000000000000101', '0000000000001000', '0000000000001101', '0000000000010101', '0000000000100010', '0000000000110111', '0000000001011001', '0000000010010000', '0000000011101001', '0000000101111001', '0000001001100010', '0000001111011011', '0000011000111101', '0000101000011000', '0001000001010101', '0001101001101101', '0010101011000010', '0100010100101111', '0110111111110001', "1011010100100000"]
    
        ass = assembler()
        cmptr = computer()

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)

        fibonacci_index = 25
        fibonacci_index -= 3
        # Init the sequence
        for x in range(10):
            cmptr.run_a_instruction("0")

        
        for y in range(fibonacci_index):
            for z in range(22):
                cmptr.run_a_instruction("0")
            self.assertEqual(fibonacci[y], cmptr.cpu.D_register.register_n_bit("0000000000000000", "0"))



if __name__ == '__main__':
    unittest.main()