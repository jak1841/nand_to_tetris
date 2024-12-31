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
    PUSH_D_INSTRUCTION = 0b1000000000000011
    PUSH_MEMORY_SEGMENT_INSTRUCTION = 0b1010000000000000
    POP_MEMORY_SEGMENT_INSTRUCTION = 0b1011000000000000 
    POP_D_INSTRUCTION = 0b1000000000000001
    CALL_INSTRUCTION = 0b1100000000000000 
    RET_INSTRUCTION = 0b1000000000000010
    PUSH_CONSTANT_INSTRUCTION = 0b10000000000000000000 

    def __init__(self):
        self.data_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address
        self.instruction_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address

         # Screen size: 112 x 176 and will be after 

        self.cpu = cpu_16_bit() # CPU using hack speceificiation 

        # Keyboard code will be using the default python so kinda cheating but idk
        self.init_inM()

    def init_inM(self):
        A_register_value = self.cpu.A_register.register_16_bit(0000000000000000, 0)
        self.inM = self.data_memory.do_operation(0000000000000000, A_register_value & 0x7FFF, 0)

    def isExtendedInstruction(self, instruction):
        if (instruction & 0xF0000 == computer.PUSH_CONSTANT_INSTRUCTION):
            return True
        if (instruction == computer.POP_D_INSTRUCTION):
            return True
        if (instruction & 0xE000 == computer.CALL_INSTRUCTION):
            return True
        if (instruction == computer.RET_INSTRUCTION):
            return True
        if (instruction & 0xF000 == computer.PUSH_MEMORY_SEGMENT_INSTRUCTION):
            return True
        if (instruction & 0xF000 == computer.POP_MEMORY_SEGMENT_INSTRUCTION):
            return True
        return instruction == computer.PUSH_D_INSTRUCTION

    def executeExtendedInstruction(self, instruction):
        if (instruction & 0xF0000 == computer.PUSH_CONSTANT_INSTRUCTION):
            self.executePushConstantInstruction(instruction)
        elif (instruction == computer.PUSH_D_INSTRUCTION):
            self.executePushDInstruction()
        elif (instruction == computer.POP_D_INSTRUCTION):
            self.executePopDInstruction()
        elif (instruction & 0xE000 == computer.CALL_INSTRUCTION):
            self.executeCallInstruction(instruction)
        elif (instruction == computer.RET_INSTRUCTION):
            self.executeRetInstruction()
        elif (instruction & 0xF000 == computer.PUSH_MEMORY_SEGMENT_INSTRUCTION):
            self.executePushMemorySegmentInstruction(instruction)
        elif (instruction & 0xF000 == computer.POP_MEMORY_SEGMENT_INSTRUCTION):
            self.executePopMemorySegmentInstruction(instruction)
        else:
            raise Exception("Unknown Extended instruction " + instruction)
        self.cpu.PC.PC_counter_16_bit(0000000000000000, 1, 0, 0) 

    def executePushDInstruction(self):
        spAddress = 0
        memory = self.data_memory.memory
        SP_value = memory[spAddress]
        D_value = self.cpu.D_register.register_16_bit(0, 0)
        memory[SP_value] = D_value
        memory[spAddress] = (SP_value + 1) & 0xFFFF

    def executePopDInstruction(self):
        spAddress = 0
        memory = self.data_memory.memory
        memory[spAddress] = (memory[spAddress] - 1) & 0xFFFF
        SP_value = memory[spAddress]
        self.cpu.D_register.register_16_bit(memory[SP_value], 1)

    def executeCallInstruction(self, instruction):
        def pushMemoryAddressValueToStack(memoryAddress):
            spAddress = 0
            memory = self.data_memory.memory
            SP_value = memory[spAddress]
            memory[SP_value] = memory[memoryAddress]
            memory[spAddress] = (SP_value + 1) & 0xFFFF
        
        spAddress = 0
        lclAddress = 1
        argAddress = 2
        thisAddress = 3
        thatAddress = 4

        pushMemoryAddressValueToStack(lclAddress)
        pushMemoryAddressValueToStack(argAddress)
        pushMemoryAddressValueToStack(thisAddress)
        pushMemoryAddressValueToStack(thatAddress)

        memory = self.data_memory.memory
        memory[lclAddress] = memory[spAddress]
        memory[argAddress] = memory[spAddress] - 5 - (instruction & 0x1FFF)

    def executeRetInstruction(self):
        def popArg0():
            argValue = memory[argAddress]
            memory[spAddress] = (memory[spAddress] - 1) & 0xFFFF
            SP_value = memory[spAddress]
            memory[argValue] = memory[SP_value]

        memory = self.data_memory.memory
        spAddress = 0
        lclAddress = 1
        argAddress = 2
        thisAddress = 3
        thatAddress = 4

        frame = memory[lclAddress] 
        ret = (memory[frame - 5] - 1) & 0xFFFF
        popArg0()
        memory[spAddress] = memory[argAddress] + 1
        memory[thatAddress] = memory[frame - 1]
        memory[thisAddress] = memory[frame - 2]
        memory[argAddress] = memory[frame - 3]
        memory[lclAddress] = memory[frame - 4]
        self.cpu.PC.PC_counter_16_bit(ret, 0, 1, 0)

    def executePushMemorySegmentInstruction(self, instruction):
        spAddress = 0
        index = instruction & 0x00FF
        memorySegmentAddress = (instruction & 0x0F00) >> 8
        memory = self.data_memory.memory
        memoryAddress = memory[memorySegmentAddress]
        SP_value = memory[spAddress]
        memory[SP_value] = memory[memoryAddress + index]
        memory[spAddress] = (SP_value + 1) & 0xFFFF

    def executePopMemorySegmentInstruction(self, instruction):
        spAddress = 0
        memory = self.data_memory.memory
        memory[spAddress] = (memory[spAddress] - 1) & 0xFFFF
        SP_value = memory[spAddress]

        index = instruction & 0x00FF
        memorySegmentAddress = (instruction & 0x0F00) >> 8

        memoryAddress = memory[memorySegmentAddress]
        memory[memoryAddress + index] = memory[SP_value]

    def executePushConstantInstruction(self, instruction):
        constant = instruction & 0x7FFF
        spAddress = 0
        memory = self.data_memory.memory
        SP_value = memory[spAddress]
        memory[SP_value] = constant
        memory[spAddress] = (SP_value + 1) & 0xFFFF

    # Runs one instruction from instructions memory starting from address 0
    def run_a_instruction(self, reset):
        PC_value = self.cpu.PC.PC_counter_16_bit(0000000000000000, 0, 0, 0) & 0x7FFF  # 15 bit is needed
        instruction = self.instruction_memory.do_operation(0000000000000000, PC_value, 0)
        if (self.isExtendedInstruction(instruction)):
            self.executeExtendedInstruction(instruction)
            return
        result_alu, writeM, addressM, PC_address = self.cpu.execute_instruction(self.inM, instruction, reset)

        self.inM = self.data_memory.do_operation(result_alu, addressM & 0x7FFF, writeM)

    # Loads the program into instructions memory to be ready to executre
    def load_program(self, array_instruction):
        self.run_a_instruction(1)     # reset program counter
        a = alu()
        position = 000000000000000

        # reset data memory and instruction memory
        self.data_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address
        self.instruction_memory = Ram_n(32768, 16) # in: 15 bit address, out: 16 bit address

        for x in array_instruction:
            binary_instruction = x
            self.instruction_memory.do_operation(binary_instruction, position, 1)
            position = a.adder_16_bit(0x1, position)

    def convertTo16BitBinaryString(self, value):
        # Convert the unsigned integer to a binary string and remove the '0b' prefix
        binary_str = bin(value)[2:]
        
        # Pad the binary string with leading zeros to make it 16 bits long
        binary_str = binary_str.zfill(16)
        
        return binary_str
        
    # Prints the RAM contents to the screen 
    def display_screen(self):

        # Gets all Ram values responsible for screen info and puts it into an screen
        display_screen = ""
        for x in range(29):
            for y in range(10):
                videoRamAddress = 16385 + (10*x) + y
                display_screen+= self.convertTo16BitBinaryString(self.data_memory.memory[videoRamAddress])
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
            self.run_a_instruction(0)

    # Gets the SP value 
    def get_sp_value(self):
        return self.data_memory.memory[0]
    
    # peeks at the top of the stack for and returns value that is on it 
    def peek_stack(self):
        a = alu()
        top_stack_address = a.alu_n_bit_operation(0b1111111111111111, self.get_sp_value(), a.ADD)[0]
        return self.data_memory.do_operation(top_stack_address, top_stack_address,  0)
