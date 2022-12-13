from central_processing_unit import cpu_16_bit
from hack_assembler import assembler


ass = assembler()

cpu = cpu_16_bit()
inM = "1110000000000000"
reset = "0"


instruction_assembly = "@7"
instruction_binary = ass.hack_assembly_instruction_to_binary_instruction(instruction_assembly)
print(cpu.execute_instruction(inM, instruction_binary, reset))
print(cpu.A_register.register_n_bit(instruction_binary, "0"))




instruction_assembly = "D=A;null"
instruction_binary = ass.hack_assembly_instruction_to_binary_instruction(instruction_assembly)
print(cpu.execute_instruction(inM, instruction_binary, reset))
print(cpu.D_register.register_n_bit(instruction_binary, "0"))

instruction_assembly = "A=D+A;null"
instruction_binary = ass.hack_assembly_instruction_to_binary_instruction(instruction_assembly)
print(cpu.execute_instruction(inM, instruction_binary, reset))


print(cpu.A_register.register_n_bit(instruction_binary, "0"))




