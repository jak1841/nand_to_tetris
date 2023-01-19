from hack_assembler import assembler
from hack_computer import computer
from Virtual_machine import Vm

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


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
cmptr.load_program(binary_program)


cmptr.run_N_number_instructions(30000)

sp = cmptr.data_memory.memory[0]
print(sp)

print(cmptr.peek_stack())
print(cmptr.data_memory.memory[256:366])

print(cmptr.data_memory.memory[:10])


# cmptr.display_screen()






