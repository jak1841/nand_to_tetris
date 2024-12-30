from arithemtic_logic_unit import alu
from random_access_memory import Ram_n
from sequential_logic import sequential
from logic_gates import gate as g

gate = g()


'''
Inputs:             inM[16],             // M value input (M = contents of RAM[A])
                    instructions[16],    // Instructions for execution
                    reset                // Signals whether to restart the current program (reset = 1)
                                         // Or continue the program (reset = 0)       


Outputs:            outM[16],           // alu output
                    writeM,             // Write to memory?
                    addressM[15],       // Address of where to write 
                    pc[15],             // updated PC counter

Function: Executes the instruction according to the Hack machine language specefication 
(SEE The Elements of Computing Systems: Building a Modern Computer from First Principles)

'''
class cpu_16_bit:
    def __init__(self):
        self.arithmetic_logic_unit = alu()
        self.D_register = sequential()
        self.A_register = sequential()
        self.PC = sequential()
    
       
    def execute_instruction(self, inM, instruction, reset):
        result_alu, zr, ng = self.do_alu_operation(instruction, inM)
        writeM = self.do_store_alu_result_operation(instruction, result_alu)
        PC_address = self.do_jump_handling_operation(zr, ng, reset, instruction)
        addressM = self.a_instruction_or_c_instruction(instruction, result_alu)
        return [result_alu, writeM, addressM, PC_address]

    # Input:    Instruction[n]
    #           InM[n]
    # Output:   [output[n], zr, ng] (Results of the ALU)
    # Function: Given the a specefic instruction and memory input then returns alu output depending
    #           On the insturctions. 
    def do_alu_operation(self, instruction, inM):
        a = (instruction >> 12) & 0x1
        A_register_value = self.A_register.register_16_bit(inM, 0) 
        A_or_inM = gate.n_bit_multipexor(A_register_value, inM, a)

        alu_operation_input = (instruction >> 6) & 0x3F
        D_register_value = self.D_register.register_16_bit(inM, 0)
        return self.arithmetic_logic_unit.alu_n_bit_operation(D_register_value, A_or_inM, alu_operation_input)
    
    # Input:    Instruction[16]
    #           Result_alu[16]
    # Output:   writeM[1]   // Returns a bit outputing if the result of alu needs to be written to memory 
    #   
    # Function: Stores the result of the alu in the correct place assuming eithier d1, d2, d3 bits are active
    #           d1 -> A register
    #           d2 -> D register
    #           d3 -> Address of M in ram (Value stored in A register)
    def do_store_alu_result_operation(self, instruction, result_alu):
        d1 = (instruction >> 5) & 0x1
        d2 = (instruction >> 4) & 0x1
        d3 = (instruction >> 3) & 0x1

        a = (instruction >> 15) & 0x1

        # if C instruction then can store 
        # else then A instruction so no storing 
        new_d1 = gate.and_(d1, a)
        new_d2 = gate.and_(d2, a)
        new_d3 = gate.and_(d3, a)

        self.A_register.register_16_bit(result_alu, new_d1)
        self.D_register.register_16_bit(result_alu, new_d2)
        return new_d3
        
    # Input:    zr[1]                   // zero flag from alu output
    #           ng[1]                   // negative flag form alu output
    #           reset[1]                // reset program counter 
    #           instruction[16]         
    # Output:   PC[16]                  // PC address for instruction memory 
    # Function: Handles the jump portion of memory given the flags      
    #           If no jump occurs increment the PC counter 
    #           if jump occurs change the PC counter address to be the value in register A
    def do_jump_handling_operation(self, zr, ng, reset, instruction):
        j1 = (instruction >> 2) & 0x1
        j2 = (instruction >> 1) & 0x1
        j3 = instruction & 0x1

        new_j1 = gate.and_(j1,  ng)
        new_j2 = gate.and_(j2, zr)
        new_j3 = gate.and_(j3, gate.and_(gate.not_(ng), gate.not_(zr)))

        r1 = gate.or_(gate.or_(new_j1, new_j2), new_j3)

        # if C instruction then can jump 
        # else then A instruction so no jumping
        first = (instruction >> 15) & 0x1
        r2 = gate.and_(first, r1)
        A_register_value = self.A_register.register_16_bit(instruction, 0)
        return self.PC.PC_counter_16_bit(A_register_value, gate.not_(r2), r2, reset)
        

    # Input:    instruction[16]
    #           alu_output[16]
    # Output:   value of register A
    # Function: if A instruction then sets Register to A to instruction 
    #           else C instruction -> sets Reigster A to alue output 
    def a_instruction_or_c_instruction(self, instruction, alu_output):
        first = (instruction >> 15) & 0x1
        r1 = gate.n_bit_multipexor(instruction, alu_output, first)
        return self.A_register.register_16_bit(r1, gate.not_(first) & 0x1)

    





    


    
    
