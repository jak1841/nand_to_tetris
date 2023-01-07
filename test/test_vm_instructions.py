import unittest
import sys


# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')

from hack_assembler import assembler
from hack_computer import computer
from Virtual_machine import Vm




class Test(unittest.TestCase):

    # converts a decimal number to its sixteen bit representation and return that binary number
    def convert_decimal_to_16_bit(self, decimal):
        result = list(str(bin(decimal)))[2:]
        empty_instruction = ["0" for x in range(16)]
        for x in range(min(len(result), 15)):
            empty_instruction[-x - 1] = result[-x - 1]
        
        return ''.join(empty_instruction)

    # converts a list of decimal number to its sixteen bit representation and return that array
    def convert_decimal_list_to_16_bit(self, list_decimal):
        ret = []
        for x in list_decimal:
            ret.append(self.convert_decimal_to_16_bit(x))
        
        return ret

    def test_arithmetic(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        vm_instructions_array = [
            "push constant 812", 
            "push constant 120", 
            "sub", 
            "push constant 210", 
            "add", 
            "push constant 2010", 
            "sub", 
            "push constant 6645", 
            "push constant 3230", 
            "sub", 
            "push constant 812", 
            "push constant 50", 
            "add", 
            "sub", 
            "add"
        ]
        
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual("0000000100000001", cmptr.data_memory.memory[0])
        self.assertEqual("0000010110100101", cmptr.data_memory.memory[256])

        

        vm_instructions_array = [
            "push constant 812", 
            "neg",
            "push constant 120", 
            "sub", 
            "push constant 210", 
            "add", 
            "push constant 2010", 
            "sub", 
            "push constant 6645", 
            "push constant 3230", 
            "sub", 
            "push constant 812", 
            "push constant 50", 
            "add", 
            "sub", 
            "add", 
            "neg"
        ]
        
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual("0000000100000001", cmptr.data_memory.memory[0])
        self.assertEqual("0000000010110011", cmptr.data_memory.memory[256])

    def test_logical(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        # evaluating if (x == 92)
        vm_instructions_array = [
            "push constant 0", 
            "push constant 92", 
            "eq"
        ]

        
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

        
        

        # evaluating if (x == 791)
        vm_instructions_array = [
            "push constant 791", 
            "push constant 791", 
            "eq"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("1111111111111111", cmptr.data_memory.memory[256])

        # evaluating if (x == 9210)
        vm_instructions_array = [
            "push constant 9210", 
            "push constant 9211", 
            "eq"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

        # evaluating if (x > 201)
        vm_instructions_array = [
            "push constant 999", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("1111111111111111", cmptr.data_memory.memory[256])

        vm_instructions_array = [
            "push constant 69", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

        vm_instructions_array = [
            "push constant 201", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 6120", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("1111111111111111", cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 6789", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 7000", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000000000000000", cmptr.data_memory.memory[256])

    def test_bitwise(self):

        ass = assembler()
        cmptr = computer()
        vm = Vm()

        # AND
        vm_instructions_array = [
            "push constant 18180", 
            "push constant 14904", 
            "and"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0000001000000000", cmptr.data_memory.memory[256])
            
        # OR
        vm_instructions_array = [
            "push constant 19017", 
            "push constant 20091", 
            "or"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("0100111001111011", cmptr.data_memory.memory[256])

        # not
        vm_instructions_array = [
            "push constant 15626",  
            "not"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual("1100001011110101", cmptr.data_memory.memory[256])

    def test_memory_access_push_constant(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()


        vm_instructions_array = ["push constant " + str(x) for x in range(1000)]


        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction("0")
        
        self.assertEqual("0000010011101000", cmptr.get_sp_value())
        self.assertEqual("0000001111100111", cmptr.peek_stack())


        vm_instructions_array = ["push constant " + str(x) for x in range(420, 912)]


        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction("0")
        
        self.assertEqual("0000001011101100", cmptr.get_sp_value())
        self.assertEqual("0000001110001111", cmptr.peek_stack())


        
    # tests the push and static vm comands  
    def test_memory_access_static(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()


        vm_instructions_array = ["push constant " + str(x) for x in range(240)]
        vm_instructions_array += ["pop static " + str(x) for x in range(240)]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction("0")
        
        self.assertEqual("0000000100000000", cmptr.get_sp_value())
        self.assertEqual("0000000000000000", cmptr.peek_stack())
        self.assertEqual([self.convert_decimal_to_16_bit(x) for x in range(240)], cmptr.data_memory.memory[16:256][::-1])


        vm_instructions_array = ["push constant " + str(x) for x in range(240)]
        vm_instructions_array += ["pop static " + str(x) for x in range(240)]
        vm_instructions_array += ["push static " + str(239 - x) for x in range(240)]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction("0")

        self.assertEqual("0000000111110000", cmptr.get_sp_value())
        self.assertEqual("0000000011101111", cmptr.peek_stack())
        self.assertEqual([self.convert_decimal_to_16_bit(x) for x in range(240)], cmptr.data_memory.memory[16:256][::-1])
        
    def test_memory_access_LCL_ARG_THIS_THAT_memory_segment(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()
        # This will be where in data memory the corresponding register will be located 
        # REGISTER -> INDEX
        # SP -> 0
        # LCL -> 1 
        # ARG -> 2
        # THIS -> 3
        # THAT -> 4


        self.assertEqual([self.convert_decimal_to_16_bit(0) for x in range(40)], cmptr.data_memory.memory[2048:2088])
        

        vm_instructions_array = ["push constant " + str(x) for x in range(69, 79)]
        vm_instructions_array += ["pop LCL " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(420, 430)]
        vm_instructions_array += ["pop ARG " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(911, 921)]
        vm_instructions_array += ["pop THIS " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(8008, 8018)]
        vm_instructions_array += ["pop THAT " + str(x) for x in range(10)]



        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        # init the values inside the registers 
        cmptr.data_memory.memory[1] = self.convert_decimal_to_16_bit(2048)  # LCL
        cmptr.data_memory.memory[2] = self.convert_decimal_to_16_bit(2058)  # ARG
        cmptr.data_memory.memory[3] = self.convert_decimal_to_16_bit(2068)  # THIS
        cmptr.data_memory.memory[4] = self.convert_decimal_to_16_bit(2078)  # THAT


        for x in range(20000):
            cmptr.run_a_instruction("0")
        
        


        self.assertEqual(self.convert_decimal_to_16_bit(256), cmptr.get_sp_value())
        self.assertEqual(["0000000100000000", "0000100000000000", "0000100000001010", "0000100000010100", "0000100000011110"], cmptr.data_memory.memory[0:5])
        self.assertEqual(self.convert_decimal_list_to_16_bit([
            78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 
            429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 
            920, 919, 918, 917, 916, 915, 914, 913, 912, 911, 
            8017, 8016, 8015, 8014, 8013, 8012, 8011, 8010, 8009, 8008
        ]), cmptr.data_memory.memory[2048:2088])


        """
            TESTING PUSHING of the function 
        
        """

        vm_instructions_array = ["push constant " + str(x) for x in range(69, 79)]
        vm_instructions_array += ["pop LCL " + str(x) for x in range(10)]
        vm_instructions_array += ["push constant " + str(x) for x in range(420, 430)]
        vm_instructions_array += ["pop ARG " + str(x) for x in range(10)]
        vm_instructions_array += ["push constant " + str(x) for x in range(911, 921)]
        vm_instructions_array += ["pop THIS " + str(x) for x in range(10)]
        vm_instructions_array += ["push constant " + str(x) for x in range(8008, 8018)]
        vm_instructions_array += ["pop THAT " + str(x) for x in range(10)]

        vm_instructions_array += ["push LCL " + str(9-x) for x in range(10)]
        vm_instructions_array += ["push ARG " + str(9-x) for x in range(10)]
        vm_instructions_array += ["push THIS " + str(9-x) for x in range(10)]
        vm_instructions_array += ["push THAT " + str(9-x) for x in range(10)]



        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        # init the values inside the registers 
        cmptr.data_memory.memory[1] = self.convert_decimal_to_16_bit(2048)  # LCL
        cmptr.data_memory.memory[2] = self.convert_decimal_to_16_bit(2058)  # ARG
        cmptr.data_memory.memory[3] = self.convert_decimal_to_16_bit(2068)  # THIS
        cmptr.data_memory.memory[4] = self.convert_decimal_to_16_bit(2078)  # THAT


        


        for x in range(20000):
            cmptr.run_a_instruction("0")

        self.assertEqual(self.convert_decimal_to_16_bit(296), cmptr.get_sp_value())
        self.assertEqual(["0000000100101000", "0000100000000000", "0000100000001010", "0000100000010100", "0000100000011110"], cmptr.data_memory.memory[0:5])
        self.assertEqual(self.convert_decimal_list_to_16_bit([
            69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
            420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 
            8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017  
            ]), cmptr.data_memory.memory[256:296])

        

    def test_memory_access_ptr_memory_segment(self):
        # ass = assembler()
        # cmptr = computer()
        # vm = Vm()


        # vm_instructions_array = [
        #     "push constant 8213",
        #     "push constant 912", 
        #     "pop" 
        # ]
        # hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        # binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
        # cmptr.load_program(binary_program)


        # self.assertEqual(self.convert_decimal_list_to_16_bit(0, 0), cmptr.data_memory.memory[3:5])


        # for x in range(5000):
        #     cmptr.run_a_instruction("0")
        pass

        
        




if __name__ == '__main__':
    unittest.main()