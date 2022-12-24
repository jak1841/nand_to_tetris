"""
    The Pinnacle of hardware, 
    Connecting the CPU, DATA memory, and Instruction memory 
"""
from random_access_memory import Ram_n
from central_processing_unit import cpu_16_bit
from arithemtic_logic_unit import alu

class computer:
    """
        DATA MEMORY 0 - 16384
        Screen - 16385- 17665           # Screen is 112 x 176
        17665 - 32768 will be null

        Instruction Memory 0 - 32768    # Readonly 




    """
    def __init__(self):
        self.data_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address
        self.instruction_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address

         # Screen size: 112 x 176 and will be after 

        self.cpu = cpu_16_bit() # CPU using hack speceificiation 

        # Keyboard code will be using the default python so kinda cheating but idk
        self.init_inM()
        


    def init_inM(self):
        A_register_value = self.cpu.A_register.register_n_bit("0000000000000000", "0")
        self.inM = self.data_memory.do_operation("0000000000000000", A_register_value[1:], "0")


    # Runs one instruction from instructions memory starting from address 0
    def run_a_instruction(self, reset):

        PC_value = self.cpu.PC.PC_counter_n_bit("0000000000000000", "0", "0", "0")[1:]  # 15 bit is needed
        instruction = self.instruction_memory.do_operation("0000000000000000", PC_value, "0")
        result_alu, writeM, addressM, PC_address = self.cpu.execute_instruction(self.inM, instruction, reset)

        self.inM = self.data_memory.do_operation(result_alu, addressM[1:], writeM)
        

    # Loads the program into instructions memory to be ready to executre
    def load_program(self, array_instruction):

        a = alu()
        position = "000000000000000"

        for x in array_instruction:
            binary_instruction = x
            self.instruction_memory.do_operation(binary_instruction, position, "1")
            position = a.increment_n_bit(position)

        

        
        



