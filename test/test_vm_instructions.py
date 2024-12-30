import unittest
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
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(0b0000000100000001, cmptr.data_memory.memory[0])
        self.assertEqual(0b0000010110100101, cmptr.data_memory.memory[256])

        

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
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(0b0000000100000001, cmptr.data_memory.memory[0])
        self.assertEqual(0b0000000010110011, cmptr.data_memory.memory[256])

        vm_instructions_array = [
            "push constant 17711", 
            "push constant 28657", 
            "add"
        ]
        
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(0b1011010100100000, cmptr.peek_stack())

        vm_instructions_array = [
            "function resp 2",
            "push constant 911", 
            "push constant 911", 
            "add"
        ]

    def test_multiplication(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        vm_instructions_array = [
            "push constant 8", 
            "push constant 7", 
            "push constant 6", 
            "push constant 5",
            "push constant 4", 
            "push constant 3", 
            "push constant 2", 
            "push constant 1",
            "mult", 
            "mult",
            "mult", 
            "mult",
            "mult", 
            "mult",
            "mult", 
            
                                 ]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(0b1001110110000000, cmptr.peek_stack())

    def test_division(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        vm_instructions_array = [
            "push constant 4096", 
            "push constant 2",
            "div",
            "push constant 2",
            "div",
            "push constant 2",
            "div",
            "push constant 2",
            "div",
            "push constant 2",
            "div",
            "push constant 8", 
            "mult", 
            "push constant 8", 
            "div",
            "push constant 2",
            "div",
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(64, cmptr.peek_stack())

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
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)

        self.assertEqual(0b0000000000000000, cmptr.data_memory.memory[256])

        
        # Local check that things are equal (x == 911)
        vm_instructions_array = [
            "function rec 2", 
            "push constant 911", 
            "pop LCL 0", 
            "push constant 911", 
            "pop LCL 1",
            "push LCL 0", 
            "push LCL 1" , 
            "eq"
        ]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b1111111111111111, cmptr.peek_stack())
        

        # evaluating if (x == 791)
        vm_instructions_array = [
            "push constant 791", 
            "push constant 791", 
            "eq"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b1111111111111111, cmptr.data_memory.memory[256])

        # evaluating if (x == 9210)
        vm_instructions_array = [
            "push constant 9210", 
            "push constant 9211", 
            "eq"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0000000000000000, cmptr.data_memory.memory[256])

        # evaluating if (x > 201)
        vm_instructions_array = [
            "push constant 999", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b1111111111111111, cmptr.data_memory.memory[256])

        vm_instructions_array = [
            "push constant 69", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0000000000000000, cmptr.data_memory.memory[256])

        vm_instructions_array = [
            "push constant 201", 
            "push constant 201", 
            "gt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0000000000000000, cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 6120", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b1111111111111111, cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 6789", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0000000000000000, cmptr.data_memory.memory[256])

        # if x < 6789
        vm_instructions_array = [
            "push constant 7000", 
            "push constant 6789", 
            "lt"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0000000000000000, cmptr.data_memory.memory[256])

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
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b0000001000000000, cmptr.data_memory.memory[256])
            
        # OR
        vm_instructions_array = [
            "push constant 19017", 
            "push constant 20091", 
            "or"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b0100111001111011, cmptr.data_memory.memory[256])

        # not
        vm_instructions_array = [
            "push constant 15626",  
            "not"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)
        cmptr.run_N_number_instructions(1000)
        self.assertEqual(0b1100001011110101, cmptr.data_memory.memory[256])

    def test_memory_access_push_constant(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()


        vm_instructions_array = ["push constant " + str(x) for x in range(1000)]


        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction(0)
        
        self.assertEqual(0b0000010011101000, cmptr.get_sp_value())
        self.assertEqual(0b0000001111100111, cmptr.peek_stack())


        vm_instructions_array = ["push constant " + str(x) for x in range(420, 912)]


        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction(0)
        
        self.assertEqual(0b0000001011101100, cmptr.get_sp_value())
        self.assertEqual(0b0000001110001111, cmptr.peek_stack())
  
    # tests the push and static vm comands  
    def test_memory_access_static(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()


        vm_instructions_array = ["push constant " + str(x) for x in range(240)]
        vm_instructions_array += ["pop static " + str(x) for x in range(240)]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction(0)
        
        self.assertEqual(0b0000000100000000, cmptr.get_sp_value())
        self.assertEqual(0000000000000000, cmptr.peek_stack())
        self.assertEqual([(x) for x in range(240)], cmptr.data_memory.memory[16:256][::-1])


        vm_instructions_array = ["push constant " + str(x) for x in range(240)]
        vm_instructions_array += ["pop static " + str(x) for x in range(240)]
        vm_instructions_array += ["push static " + str(239 - x) for x in range(240)]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)

        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        for x in range(10000):
            cmptr.run_a_instruction(0)

        self.assertEqual(0b0000000111110000, cmptr.get_sp_value())
        self.assertEqual(0b0000000011101111, cmptr.peek_stack())
        self.assertEqual([(x) for x in range(240)], cmptr.data_memory.memory[16:256][::-1])
        
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


        self.assertEqual([(0) for x in range(40)], cmptr.data_memory.memory[2048:2088])
        

        vm_instructions_array = ["push constant " + str(x) for x in range(69, 79)]
        vm_instructions_array += ["pop LCL " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(420, 430)]
        vm_instructions_array += ["pop ARG " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(911, 921)]
        vm_instructions_array += ["pop THIS " + str(x) for x in range(10)]

        vm_instructions_array += ["push constant " + str(x) for x in range(8008, 8018)]
        vm_instructions_array += ["pop THAT " + str(x) for x in range(10)]



        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        # init the values inside the registers 
        cmptr.data_memory.memory[1] = (2048)  # LCL
        cmptr.data_memory.memory[2] = (2058)  # ARG
        cmptr.data_memory.memory[3] = (2068)  # THIS
        cmptr.data_memory.memory[4] = (2078)  # THAT


        
        cmptr.run_N_number_instructions(10000)
        
        


        self.assertEqual((256), cmptr.get_sp_value())
        self.assertEqual([0b0000000100000000, 0b0000100000000000, 0b0000100000001010, 0b0000100000010100, 0b0000100000011110], cmptr.data_memory.memory[0:5])
        self.assertEqual([
            78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 
            429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 
            920, 919, 918, 917, 916, 915, 914, 913, 912, 911, 
            8017, 8016, 8015, 8014, 8013, 8012, 8011, 8010, 8009, 8008
        ], cmptr.data_memory.memory[2048:2088])


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




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        # init the values inside the registers 
        cmptr.data_memory.memory[1] = (2048)  # LCL
        cmptr.data_memory.memory[2] = (2058)  # ARG
        cmptr.data_memory.memory[3] = (2068)  # THIS
        cmptr.data_memory.memory[4] = (2078)  # THAT

    

        for x in range(10000):
            cmptr.run_a_instruction(0)

        self.assertEqual((296), cmptr.get_sp_value())
        self.assertEqual([0b0000000100101000, 0b0000100000000000, 0b0000100000001010, 0b0000100000010100, 0b0000100000011110], cmptr.data_memory.memory[0:5])
        self.assertEqual([
            69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
            420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 
            8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017  
            ], cmptr.data_memory.memory[256:296])

    def test_memory_access_ptr_memory_segment(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()


        vm_instructions_array = [
            "push constant 8213",
            "push constant 2069", 
            "pop PTR 0", 
            "pop PTR 1"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        self.assertEqual([0, 0], cmptr.data_memory.memory[3:5])


        for x in range(1000):
            cmptr.run_a_instruction(0)

        
        self.assertEqual([2069, 8213], cmptr.data_memory.memory[3:5])
        self.assertEqual((256), cmptr.get_sp_value())

        vm_instructions_array = [
            "push constant 9210",
            "push constant 2100", 
            "pop PTR 0", 
            "pop PTR 1", 
            "push PTR 1", 
            "push PTR 0", 
            "push PTR 1"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)


        self.assertEqual([0, 0], cmptr.data_memory.memory[3:5])


        for x in range(1000):
            cmptr.run_a_instruction(0)

        
        self.assertEqual([2100, 9210], cmptr.data_memory.memory[3:5])
        self.assertEqual((259), cmptr.get_sp_value())
        self.assertEqual((9210), cmptr.peek_stack())
        self.assertEqual([9210, 2100, 9210], cmptr.data_memory.memory[256:259])
        
    def test_memory_acccess_temp_memory_segment(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        vm_instructions_array = [
            "push constant 9688",
            "push constant 15868", 
            "push constant 5806", 
            "push constant 12661", 
            "push constant 14612", 
            "push constant 129", 
            "push constant 19462", 
            "push constant 13738", 
            "pop TEMP 0", 
            "pop TEMP 1", 
            "pop TEMP 2", 
            "pop TEMP 3",
            "pop TEMP 4",
            "pop TEMP 5",
            "pop TEMP 6",
            "pop TEMP 7" 

        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0], cmptr.data_memory.memory[5:13])


        for x in range(1000):
            cmptr.run_a_instruction(0)
        
        array = [9688, 15868, 5806, 12661, 14612, 129, 19462, 13738]
        self.assertEqual((array[::-1]), cmptr.data_memory.memory[5:13])
        self.assertEqual((256), cmptr.get_sp_value())

        vm_instructions_array = [
            "push constant 9688",
            "push constant 15868", 
            "push constant 5806", 
            "push constant 12661", 
            "push constant 14612", 
            "push constant 129", 
            "push constant 19462", 
            "push constant 13738", 
            "pop TEMP 0", 
            "pop TEMP 1", 
            "pop TEMP 2", 
            "pop TEMP 3",
            "pop TEMP 4",
            "pop TEMP 5",
            "pop TEMP 6",
            "pop TEMP 7", 
            "push TEMP 7", 
            "push TEMP 6", 
            "push TEMP 5", 
            "push TEMP 4", 
            "push TEMP 3", 
            "push TEMP 2", 
            "push TEMP 1", 
            "push TEMP 0"

        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0], cmptr.data_memory.memory[5:13])


        for x in range(1000):
            cmptr.run_a_instruction(0)
        
        array = [9688, 15868, 5806, 12661, 14612, 129, 19462, 13738]
        self.assertEqual(array[::-1], cmptr.data_memory.memory[5:13])
        self.assertEqual(array, cmptr.data_memory.memory[256:264])
        self.assertEqual((264), cmptr.get_sp_value())
        self.assertEqual((13738), cmptr.peek_stack())

    # basic loop which calculates value for 1 + 2 + ... + n 
    def test_basic_loop_program(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()
        n = "50"
        vm_instructions_array = [
            "label push_value_n",
            "push constant " + n,
            "push constant " + n,
            "pop TEMP 0", 
            "pop TEMP 1", 

            "label store_one_less_in_0_add",
            "push TEMP 0", 
            "push constant 1", 
            "sub", 
            "pop TEMP 0", 
            "push TEMP 0", 
            "push TEMP 1", 
            "add", 
            "pop TEMP 1",
            
            "label comparison", 
            "push TEMP 0", 
            "push constant 0", 
            "eq", 
            "if-goto bruh", 
            "pop TEMP 2",
            "goto store_one_less_in_0_add",

            "label bruh", 
            "pop TEMP 2",
            "push TEMP 1",
            "label end", 
            "goto end"

        ]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        for x in range(9000):
            cmptr.run_a_instruction(0)
        
        self.assertEqual(0b0000010011111011, cmptr.data_memory.memory[6])
        self.assertEqual(0b0000000100000001, cmptr.get_sp_value())
        self.assertEqual(0b0000010011111011, cmptr.peek_stack())

    #  Fibonacci: computes and stores in memory the first n elements of the Fibonacci series. This typical
    #  array manipulation program provides a more challenging test of the VM’s branching commands.
    def test_Fibonnacci_program(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()
        n = "24"
        vm_instructions_array = [
            "label init_n_value", 
            "push constant " + n,
            "pop TEMP 0", 


            "label init_THIS_and_THAT_addresses",
            "push constant 2048", 
            "pop PTR 0",
            "push constant 2049", 
            "pop PTR 1",

            "label init_fibonacci_seqeunce",
            "push constant 0",
            "pop THIS 0", 
            "push constant 1",
            "pop THAT 0", 

            "label loop_conditional", 
            "push TEMP 0", 
            "push constant 1", 
            "sub", 
            "pop TEMP 0",
            "push TEMP 0", 
            "push constant 0", 
            "eq", 
            "if-goto end",


            "label add_this_that_value_and_store_on_stack", 
            "push THIS 0", 
            "push THAT 0", 
            "add",

            "label increment_THIS_THAT_ADDRESS", 
            "push constant 1", 
            "push PTR 0", 
            "add", 
            "pop PTR 0",
            "push constant 1", 
            "push PTR 1", 
            "add", 
            "pop PTR 1",


            "label store_next_fibonacci_number_to_memory", 
            "pop THAT 0",
            "goto loop_conditional",

            
            "label end", 
            "goto end"

        ]

        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)




        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        for x in range(12000):
            cmptr.run_a_instruction(0)
        
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233,377,610,987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368], cmptr.data_memory.memory[2048:2073])
        
    # Implements the multiplication function using addition 
    def test_multiplication_and_factorial_program(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        vm_instructions_array = [
            "function sys.init 0", 
            "push constant 7",
            "call fact 1",
            "push constant 6", 
            "call mult 2",
            "label end", 
            "goto end",



            "function fact 2", 
            "push constant 1", 
            "pop LCL 0", 
            "push constant 1", 
            "pop LCL 1", 
            "label loop", 
            "push constant 1", 
            "push LCL 1", 
            "add", 
            "pop LCL 1", 
            "push LCL 1", 
            "push ARG 0", 
            "gt", 
            "if-goto end", 
            "push LCL 0", 
            "push LCL 1", 
            "call mult 2", 
            "pop LCL 0", 
            "goto loop", 
            "label end", 
            "push LCL 0", 
            "return",



            "function mult 2", 
            "push constant 0", 
            "pop LCL 0", 
            "push ARG 1", 
            "pop LCL 1", 

            "label loop", 
            "push constant 0", 
            "push LCL 1", 
            "eq", 
            "if-goto end", 
            "push LCL 0", 
            "push ARG 0", 
            "add", 
            "pop LCL 0", 
            "push LCL 1", 
            "push constant 1", 
            "sub", 
            "pop LCL 1", 
            "goto loop", 

            "label end", 
            "push LCL 0", 
            "return"
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        cmptr.run_N_number_instructions(15000)

        self.assertEqual(cmptr.get_sp_value(), (257))
        self.assertEqual(cmptr.peek_stack(), (30240))


    # FIBONACCI SEQUENCE program but uses recursion 
    def test_fibonacci_recursion(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()
        n = "100"
        vm_instructions_array = [
            "push constant 0",
            "push constant " + n,
            "call rec 2",
            

            "label end", 
            "goto end",

            "function rec 0", 
            "push ARG 1",
            "push constant 0", 
            "eq", 
            "if-goto end", 
            
            "push ARG 1", 
            "push ARG 0", 
            "add", 
            "push ARG 1", 
            "push constant 1", 
            "sub", 
            "call rec 2", 
            "return",



            "label end",
            "push ARG 0",
            "return",
                        
            
        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        cmptr.run_N_number_instructions(25000)

        self.assertEqual(0b0001001110111010, cmptr.peek_stack())


    # TEST STATIC PROGRAM where we store the nth oddd number in static 0 where n is indexed 0
    def test_static_VM_program(self):
        ass = assembler()
        cmptr = computer()
        vm = Vm()

        n = "69"
        vm_instructions_array = [
            "function sys.init 0", 
            "push constant " + n, 
            "push constant 1", 
            "pop static 0",
            "call odd_number 1",

            "label end", 
            "goto end", 

            "function odd_number 0", 

            "label comparison", 
            "push constant 0", 
            "push ARG 0", 
            "eq", 
            "if-goto end",

            "label decrement",
            "pop TEMP 7", 
            "push ARG 0", 
            "push constant 1", 
            "sub", 
            "pop ARG 0",



            "label add", 
            "push constant 2", 
            "push static 0", 
            "add", 
            "pop static 0",

            "goto comparison",
            


            "label end", 
            "push constant 0",
            "return"



        ]
        hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)
        binary_program = ass.convertArrayAssemblyToBinary(hack_assembly_instructions_array)
        cmptr.load_program(binary_program)

        cmptr.run_N_number_instructions(15000)
        self.assertEqual(cmptr.data_memory.memory[16], 0b0000000010001011)




if __name__ == '__main__':
    unittest.main()