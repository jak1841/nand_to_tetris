from hack_assembler import assembler
from hack_computer import computer
from Virtual_machine import Vm

ass = assembler()
cmptr = computer()
vm = Vm()

    # program = None
    # with open('src/program.asm') as my_file:
    #     program = my_file.readlines()



    # no_whitespace_program = []
    # for x in program:
    #     no_whitespace_program.append(x.strip())

    # print(no_whitespace_program)


for x in range(100):
    vm.add_push_constant_hack_assembly(x)

hack_assembly_instructions = vm.get_assembly_instruction()


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions)
cmptr.load_program(binary_program)


for x in range(1000):
    cmptr.run_a_instruction("0")


print(cmptr.data_memory.memory[0])
print(cmptr.data_memory.memory[256:356])

# cmptr.display_screen()






