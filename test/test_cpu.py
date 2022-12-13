
import unittest
import sys

# allows use of
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')
from central_processing_unit import cpu_16_bit
from hack_assembler import assembler

cpu = cpu_16_bit()
assem = assembler()

class Test(unittest.TestCase):
    def test_cpu_comp_operation(self):
        # Initial Register and PC test 
        self.assertEqual("0000000000000000", cpu.A_register.register_n_bit("0000000000000000", "0"))
        self.assertEqual("0000000000000000", cpu.D_register.register_n_bit("0000000000000000", "0"))
        self.assertEqual("0000000000000000", cpu.PC.register_n_bit("0000000000000000", "0"))

        # 0
        inM, reset = "0000000000000000", "0"
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=0;null")
        self.assertEqual(["0000000000000000", "0", "0000000000000000", "0000000000000001"], cpu.execute_instruction(inM, instruction, reset))
        
        # 1
        inM, reset = "0000000000000000", "0"
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=1;null")
        self.assertEqual(["0000000000000001", "0", "0000000000000000", "0000000000000010"], cpu.execute_instruction(inM, instruction, reset))

        # -1
        inM, reset = "0000000000000000", "0"
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=-1;null")
        self.assertEqual(["1111111111111111", "0", "0000000000000000", "0000000000000011"], cpu.execute_instruction(inM, instruction, reset))



        # Assigning values to the game
        inM, reset = "0000000000000000", "0"
        instruction = assem.hack_assembly_instruction_to_binary_instruction("@169")
        cpu.execute_instruction(inM, instruction, reset)
        instruction = assem.hack_assembly_instruction_to_binary_instruction("D=A;null")
        cpu.execute_instruction(inM, instruction, reset)
        instruction = assem.hack_assembly_instruction_to_binary_instruction("@911")
        cpu.execute_instruction(inM, instruction, reset)
        self.assertEqual("0000001110001111", cpu.A_register.register_n_bit("0000000000000000", "0"))
        self.assertEqual("0000000010101001", cpu.D_register.register_n_bit("0000000000000000", "0"))
        self.assertEqual("0000000000000110", cpu.PC.register_n_bit("0000000000000000", "0"))

        # D
        inM, reset = "0000000000000000", "0"
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D;null")
        self.assertEqual(["0000000010101001", "0", "0000001110001111", "0000000000000111"], cpu.execute_instruction(inM, instruction, reset))


        # A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=A;null")
        self.assertEqual(["0000001110001111", "0", "0000001110001111", "0000000000001000"], cpu.execute_instruction(inM, instruction, reset))

        # !D
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=!D;null")
        self.assertEqual(["1111111101010110", "0", "0000001110001111", "0000000000001001"], cpu.execute_instruction(inM, instruction, reset))

        # !A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=!A;null")
        self.assertEqual(["1111110001110000", "0", "0000001110001111", "0000000000001010"], cpu.execute_instruction(inM, instruction, reset))

        # -D
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=-D;null")
        self.assertEqual(["1111111101010111", "0", "0000001110001111", "0000000000001011"], cpu.execute_instruction(inM, instruction, reset))

        # -A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=-A;null")
        self.assertEqual(["1111110001110001", "0", "0000001110001111", "0000000000001100"], cpu.execute_instruction(inM, instruction, reset))

        # D+1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D+1;null")
        self.assertEqual(["0000000010101010", "0", "0000001110001111", "0000000000001101"], cpu.execute_instruction(inM, instruction, reset))

        # A+1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=A+1;null")
        self.assertEqual(["0000001110010000", "0", "0000001110001111", "0000000000001110"], cpu.execute_instruction(inM, instruction, reset))

        # D-1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D-1;null")
        self.assertEqual(["0000000010101000", "0", "0000001110001111", "0000000000001111"], cpu.execute_instruction(inM, instruction, reset))

        # A-1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=A-1;null")
        self.assertEqual(["0000001110001110", "0", "0000001110001111", "0000000000010000"], cpu.execute_instruction(inM, instruction, reset))

        # D+A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D+A;null")
        self.assertEqual(["0000010000111000", "0", "0000001110001111", "0000000000010001"], cpu.execute_instruction(inM, instruction, reset))

        # D-A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D-A;null")
        self.assertEqual(["1111110100011010", "0", "0000001110001111", "0000000000010010"], cpu.execute_instruction(inM, instruction, reset))

        # A-D
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=A-D;null")
        self.assertEqual(["0000001011100110", "0", "0000001110001111", "0000000000010011"], cpu.execute_instruction(inM, instruction, reset))

        # D&A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D&A;null")
        self.assertEqual(["0000000010001001", "0", "0000001110001111", "0000000000010100"], cpu.execute_instruction(inM, instruction, reset))

        # D|A
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D|A;null")
        self.assertEqual(["0000001110101111", "0", "0000001110001111", "0000000000010101"], cpu.execute_instruction(inM, instruction, reset))



        inM, reset = "1101011010011111", "0"
        # M 
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=M;null")
        self.assertEqual(["1101011010011111", "0", "0000001110001111", "0000000000010110"], cpu.execute_instruction(inM, instruction, reset))

        # !M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=!M;null")
        self.assertEqual(["0010100101100000", "0", "0000001110001111", "0000000000010111"], cpu.execute_instruction(inM, instruction, reset))

        # -M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=-M;null")
        self.assertEqual(["0010100101100001", "0", "0000001110001111", "0000000000011000"], cpu.execute_instruction(inM, instruction, reset))

        # M+1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=M+1;null")
        self.assertEqual(["1101011010100000", "0", "0000001110001111", "0000000000011001"], cpu.execute_instruction(inM, instruction, reset))

        # M-1
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=M-1;null")
        self.assertEqual(["1101011010011110", "0", "0000001110001111", "0000000000011010"], cpu.execute_instruction(inM, instruction, reset))

        # D+M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D+M;null")
        self.assertEqual(["1101011101001000", "0", "0000001110001111", "0000000000011011"], cpu.execute_instruction(inM, instruction, reset))

        # D-M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D-M;null")
        self.assertEqual(["0010101000001010", "0", "0000001110001111", "0000000000011100"], cpu.execute_instruction(inM, instruction, reset))

        # M-D
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=M-D;null")
        self.assertEqual(["1101010111110110", "0", "0000001110001111", "0000000000011101"], cpu.execute_instruction(inM, instruction, reset))

        # D&M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D&M;null")
        self.assertEqual(["0000000010001001", "0", "0000001110001111", "0000000000011110"], cpu.execute_instruction(inM, instruction, reset))

        # D|M
        instruction = assem.hack_assembly_instruction_to_binary_instruction("null=D|M;null")
        self.assertEqual(["1101011010111111", "0", "0000001110001111", "0000000000011111"], cpu.execute_instruction(inM, instruction, reset))


        # M: 1101011010011111
        # D: 0000000010101001





if __name__ == '__main__':
    unittest.main()