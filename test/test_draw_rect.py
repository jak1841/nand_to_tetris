from hack_assembler import assembler
from hack_computer import computer

ass = assembler()
cmptr = computer()
print("Should be a rectangle drawn here")
program = None
with open('test/rect.asm') as my_file:
    program = my_file.readlines()



no_whitespace_program = []
for x in program:
    no_whitespace_program.append(x.strip())


binary_program = ass.array_hack_assembly_instruction_to_binary_instruction(no_whitespace_program)
cmptr.load_program(binary_program)


for x in range(1000):
    cmptr.run_a_instruction("0")

cmptr.display_screen()






