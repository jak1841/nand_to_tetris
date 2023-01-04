import unittest
import sys


# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')

from hack_assembler import assembler
from hack_computer import computer
from Virtual_machine import Vm




class Test(unittest.TestCase):
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
        
        

if __name__ == '__main__':
    unittest.main()