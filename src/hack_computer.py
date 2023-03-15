"""
    The Pinnacle of hardware, 
    Connecting the CPU, DATA memory, and Instruction memory 
"""
from random_access_memory import Ram_n
from central_processing_unit import cpu_16_bit
from arithemtic_logic_unit import alu
import sys
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
        self.run_a_instruction("1")     # reset program counter
        a = alu()
        position = "000000000000000"

        # reset data memory and instruction memory
        self.data_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address
        self.instruction_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address

        for x in array_instruction:
            binary_instruction = x
            self.instruction_memory.do_operation(binary_instruction, position, "1")
            position = a.increment_n_bit(position)

        
    # Prints the RAM contents to the screen 
    def display_screen(self):

        # Gets all Ram values responsible for screen info and puts it into an screen
        display_screen = ""
        for x in range(29):
            for y in range(10):
                display_screen+= self.data_memory.memory[16385 + (10*x) + y]
            display_screen+= "\n"
        
        # Convert all ones and zeros to pixels 
        pixel_screen = ""
        for x in display_screen:
            if (x == "1"):
                pixel_screen+= u"\u2588"
            elif(x == "\n"):
                pixel_screen+="\n"
            else:
                pixel_screen += " "
        

        
        print(pixel_screen)


    def clear_screen(self):
        for x in range(30):
            sys.stdout.write('\x1b[1A')
            #delete last line
            sys.stdout.write('\x1b[2K')       

    # Runs computer how ever many instruction given
    def run_N_number_instructions(self, N):
        for x in range(N):
            self.run_a_instruction("0")


    # Gets the SP value 
    def get_sp_value(self):
        return self.data_memory.memory[0]
    
    # peeks at the top of the stack for and returns value that is on it 
    def peek_stack(self):
        a = alu()
        top_stack_address = a.alu_n_bit_operation("1111111111111111", self.get_sp_value(), a.ADD)[0]
        return self.data_memory.do_operation(top_stack_address, top_stack_address,  "0")
        



