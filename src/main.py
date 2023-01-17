from hack_assembler import assembler
from hack_computer import computer
from Virtual_machine import Vm

ass = assembler()
cmptr = computer()
vm = Vm()



vm_instructions_array = [   
    "function sys.init 0", 
    "push constant 10",
    "call add_ten 1", 

    "push constant 23", 
    "sub",
    "label end", 
    "goto end",

    "function add_ten 0", 
    "push constant 23", 
    "push ARG 0",
    "add", 
    "return",
    "label end", 
    "goto end"
    
    
    
]


hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
cmptr.load_program(binary_program)


cmptr.run_N_number_instructions(3000)

sp = cmptr.data_memory.memory[0]
print(sp)

print(cmptr.peek_stack())
print(cmptr.data_memory.memory[256:366])

print(cmptr.data_memory.memory[:10])


# cmptr.display_screen()






