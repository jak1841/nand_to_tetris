import unittest
from hack_assembler import assembler
from hack_computer import computer

class Test(unittest.TestCase):
    def test_fibonacci_program(self):
        program = ['', '@first_num', 'M=0', '@second_num', 'M=1', '(add_two_previous_store_in_total)', '@total', 'M=0', '@first_num', 'D=M', '@second_num', 'D=D+M', '@total', 'M=D', '(update_previous_two_values)', '', '', '@second_num', 'D=M', '@first_num', 'M=D', '@total', 'D=M', '@second_num', 'M=D', '// This is extended due to no reason lol', '(a_has_first_and_d_has_second)', '@second_num', 'D=M', '@first_num', 'A=M', '@add_two_previous_store_in_total', '0;JMP']
        fibonacci = [0b0000000000000010, 0b0000000000000011, 0b0000000000000101, 0b0000000000001000, 0b0000000000001101, 0b0000000000010101, 0b0000000000100010, 0b0000000000110111, 0b0000000001011001, 0b0000000010010000, 0b0000000011101001, 0b0000000101111001, 0b0000001001100010, 0b0000001111011011, 0b0000011000111101, 0b0000101000011000, 0b0001000001010101, 0b0001101001101101, 0b0010101011000010, 0b0100010100101111, 0b0110111111110001, 0b1011010100100000]
    
        ass = assembler()
        cmptr = computer()

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)

        fibonacci_index = 25
        fibonacci_index -= 3
        # Init the sequence
        for x in range(10):
            cmptr.run_a_instruction(0)

        
        for y in range(fibonacci_index):
            for z in range(22):
                cmptr.run_a_instruction(0)
            self.assertEqual(fibonacci[y], cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

    def test_predefined_symbols(self):
        predefined_symbol_addresses = [0000000000000000, 0b0000000000000001, 0b0000000000000010, 
        0b0000000000000011, 0b0000000000000100, 0000000000000000, 0b0000000000000001, 0b0000000000000010, 
        0b0000000000000011, 0b0000000000000100, 0b0000000000000101, 0b0000000000000110, 0b0000000000000111, 
        0b0000000000001000, 0b0000000000001001, 0b0000000000001010, 0b0000000000001011, 0b0000000000001100, 
        0b0000000000001101, 0b0000000000001110, 0b0000000000001111, 0b0100000000000001]

        program = ['// We will be using each of the predefined symbols to check they work properyl', '', '@SP', 
        '@LCL', '@ARG', '@THIS', '@THAT', '', '', "// Bunch of R's", '@R0', '@R1', '@R2', '@R3', '@R4', '@R5', 
        '@R6', '@R7', '@R8', '@R9', '@R10', '@R11', '@R12', '@R13', '@R14', '@R15', '', '// Screen', '@SCREEN']

        ass = assembler()
        cmptr = computer()

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)

        for x in range(22):
            cmptr.run_a_instruction(0)
            self.assertEqual(predefined_symbol_addresses[x], cmptr.cpu.A_register.register_16_bit(0000000000000000, 0))

    def test_multiplication_program(self):
        program = [
            "@201", 
            "D=A", 
            "@100", 
            "D=D*A"
        ]
        ass = assembler()
        cmptr = computer()
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(20100, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@0", 
            "D=A", 
            "@1911", 
            "D=D*A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(0, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))


        program = [
            "@1", 
            "D=A", 
            "@12211", 
            "D=D*A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(12211, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@821", 
            "D=A", 
            "@50", 
            "D=D*A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(41050, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "D=0", 
            "D=D-1", 
            "@821", 
            "D=D*A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(64715, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))


        program = [
            "@31", 
            "D=A", 
            "@1902",
            "M=D*A" 
        ]
        

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(58962, cmptr.data_memory.memory[1902])

    def test_division_programs(self):
        program = [
            "@200", 
            "D=A", 
            "@100", 
            "D=D/A"
        ]
        ass = assembler()
        cmptr = computer()
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(2, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))


        program = [
            "@0", 
            "D=A", 
            "@1911", 
            "D=D/A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(0, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@1", 
            "D=A", 
            "@1911", 
            "D=D/A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(0, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@12211", 
            "D=A", 
            "@1", 
            "D=D/A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(12211, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@821",
            "D=A", 
            "A=0", 
            "A=A-1", 
            "D=D/A"
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(5)
        self.assertEqual(64715, cmptr.cpu.D_register.register_16_bit(0000000000000000, 0))

        program = [
            "@1902", 
            "D=A", 
            "@317",
            "M=D/A" 
        ]

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(program)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(4)
        self.assertEqual(6, cmptr.data_memory.memory[317])




if __name__ == '__main__':
    unittest.main()