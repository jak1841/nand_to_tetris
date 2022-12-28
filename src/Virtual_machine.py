"""
    This file will take in a virtual machine commands which uses stack based model 
    and then will translate it to hack_assembler model

    RAM USAGE: 
        0-15            Sixteen virtual registers sp, lcl, r0-15, etc
        16-255          Static variables (of all the VM functions in the VM program)
        256-2047        Stack
        2048-16483      Heap (Used to store objects and arrays)
        16384-24575     Memory mapped I/O (Keyboard, Screen)

    Stack grow upwards 
        Push x:   
            store x at sp, 
            increment sp
        
        Pop: 
            decrementing sp
            returning the value stored in top position

        Note:   Stack pointer will always point to the top of stack and therefore an
                "Empty" position 
    
    Stack Arithemtic and logical commands 
        Operands are popped from the stack and the results are pushed onto it

        

        add ->  x + y 
        sub ->  x - y
        neg ->  -y
        eq  ->  true if x = y else false
        gt  ->  true if x > y else false 
        lt  ->  true if x < y else false 
        and ->  x AND y 
        or  ->  x OR y 
        not ->  not y

        Note: 
            3 of the commands listed return true and false which the VM will represent as 
            0xFFFF (True) and 0x0000 (False) 

            y operand will be located at top of the stack 
            x operand will be located right below the top of the stack 
        
        Push constant x 
            assuming x is in decimal form will push binary representation of x 
            onto the stack  

"""

class Vm:
    def __init__(self):
        self.assembly_instructions = []         # array will contain all the assembly instructions so far used in the project
        self.add_set_sp_hack_assembly()


    # Input:            Decimal between 0-2^15
    # Output:           appends all instructions which put the constant onto the stack
    def add_push_constant_hack_assembly(self, constant):
        self.assembly_instructions += ["@" + str(constant), 
                            "D=A", 
                            "@SP", 
                            "A=M",  
                            "M=D",
                            "D=A+1", 
                            "@SP",
                            "M=D"]
    
    # appends all instructiosn which set value at sp memory address to 256
    def add_set_sp_hack_assembly(self):
        self.assembly_instructions += ["@256", 
                "D=A", 
                "@SP", 
                "M=D"]
    
    # returns the assembly instruction
    def get_assembly_instruction(self):
        return self.assembly_instructions


