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


vm_instructions_array = ["push constant " + str(x) for x in range(100)]
vm_instructions_array.append("not")

hack_assembly_instructions_array = vm.get_hack_assembly_instructions_from_VM_instructions(vm_instructions_array)


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(hack_assembly_instructions_array)
cmptr.load_program(binary_program)


for x in range(1000):
    cmptr.run_a_instruction("0")


print(cmptr.data_memory.memory[0])
print(cmptr.data_memory.memory[256:356])

# cmptr.display_screen()






