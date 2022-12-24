from hack_assembler import assembler
from hack_computer import computer


ass = assembler()
cmptr = computer()

program = None
with open('src/program.asm') as my_file:
    program = my_file.readlines()



no_whitespace_program = []
for x in program:
    no_whitespace_program.append(x.strip())

print(no_whitespace_program)


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(no_whitespace_program)
cmptr.load_program(binary_program)


for x in range(17):
    cmptr.run_a_instruction("0")

print(cmptr.cpu.A_register.register_n_bit("0000000000000000", "0"))
print(cmptr.cpu.D_register.register_n_bit("0000000000000000", "0"))
print(cmptr.cpu.PC.PC_counter_n_bit("0000000000000000", "0", "0", "0"))








