"""
    This file will take in a virtual machine commands which uses stack based model 
    and then will translate it to hack_assembler model

    # R13-R15 are general purpose virtual registers that can be used for any purpose

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

        self.label_num = 0                      # Used to create unique labels to be used for comparison operations 


    # Input:            Decimal between 0-2^15
    # Output:           appends all instructions which put the constant onto the stack
    def add_push_constant_hack_assembly(self, constant):
        self.assembly_instructions += ["@" + str(constant), 
                            "D=A"]
        
        self.add_push_d_register_value_to_stack_hack_assembly()
                            
    
    # appends all instructions which set value at sp memory address to 256
    def add_set_sp_hack_assembly(self):
        self.assembly_instructions += ["@256", 
                "D=A", 
                "@SP", 
                "M=D"]
    
    # appends all instructions which pops x, y from stack and pushes bitwise x&y to stack
    def add_and_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        #X & Y stored in D
        self.assembly_instructions += [
            "@R13", 
            "D=D&M"
        ]

        self.add_push_d_register_value_to_stack_hack_assembly()

    # appends all instructions which pops x, y from stack and pushes bitwise x|y to stack 
    def add_or_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # X|Y stored in D
        self.assembly_instructions += [
            "@R13", 
            "D=D|M"
        ]

        self.add_push_d_register_value_to_stack_hack_assembly()

    # appends all instructions which pops y from stack and pushes !y to stack
    def add_not_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()
        self.assembly_instructions += [
            "D=!D"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

    # appends all instructions which pops y from stack and pushes -y to stack
    def add_negative_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()
        self.assembly_instructions += [
            "D=-D"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

        
    # appends all instructions which pops x, y from stack and pushes x+y to stack 
    def add_addition_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Addition of X and Y stored in D
        self.assembly_instructions += [
            "@R13", 
            "D=D+M"
        ]

        self.add_push_d_register_value_to_stack_hack_assembly()

    # appends all instructions which pops x, y from stack and pushs x-y to stack 
    def add_substraction_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store x-y in register D
        self.assembly_instructions += [
            "@R13", 
            "D=D-M"
        ]

        self.add_push_d_register_value_to_stack_hack_assembly()

    
    # appends all instructions which pops x, y from stack and pushes true if x=y else false
    def add_equal_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store x-y in register D
        self.assembly_instructions += [
            "@R13", 
            "D=D-M"
        ]
        
        # Stores true or false in Register D if x = y
        self.assembly_instructions += [
            "@" + "comparison_true" + str(self.label_num),
            "D;JEQ",
            "(comparison_false" + str(self.label_num) + ")", 
            "D=0",
            "@" + "end_comparison"+ str(self.label_num),
            "0;JMP",
            "(comparison_true" + str(self.label_num) + ")",
            "D=0", 
            "D=D-1",
            "(end_comparison"+ str(self.label_num) + ")"
        ]



        self.label_num+= 1              # Increment it to make sure all comparison labels are unique
        self.add_push_d_register_value_to_stack_hack_assembly()


    # appends all instructions which pops x, y from stack and pushes true if x > y else false
    def add_greater_than_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store x-y in register D
        self.assembly_instructions += [
            "@R13", 
            "D=D-M"
        ]
        
        # Stores true or false in Register D if x = y
        self.assembly_instructions += [
            "@" + "comparison_true" + str(self.label_num),
            "D;JGT",
            "(comparison_false" + str(self.label_num) + ")", 
            "D=0",
            "@" + "end_comparison"+ str(self.label_num),
            "0;JMP",
            "(comparison_true" + str(self.label_num) + ")",
            "D=0", 
            "D=D-1",
            "(end_comparison"+ str(self.label_num) + ")"
        ]



        self.label_num+= 1              # Increment it to make sure all comparison labels are unique
        self.add_push_d_register_value_to_stack_hack_assembly()


    def add_less_than_hack_assembly(self):
        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store Y into R13
        self.assembly_instructions += [
            "@R13", 
            "M=D"
        ]

        self.add_pop_value_from_stack_to_register_d_hack_assembly()

        # Store x-y in register D
        self.assembly_instructions += [
            "@R13", 
            "D=D-M"
        ]
        
        # Stores true or false in Register D if x = y
        self.assembly_instructions += [
            "@" + "comparison_true" + str(self.label_num),
            "D;JLT",
            "(comparison_false" + str(self.label_num) + ")", 
            "D=0",
            "@" + "end_comparison"+ str(self.label_num),
            "0;JMP",
            "(comparison_true" + str(self.label_num) + ")",
            "D=0", 
            "D=D-1",
            "(end_comparison"+ str(self.label_num) + ")"
        ]



        self.label_num+= 1              # Increment it to make sure all comparison labels are unique
        self.add_push_d_register_value_to_stack_hack_assembly()

    # appends all the hack instructions required to get value in Register D pushed to the stack 
    def add_push_d_register_value_to_stack_hack_assembly(self):

        # Store D at the top of stack
        self.assembly_instructions += [
            "@SP", 
            "A=M", 
            "M=D"
        ]

        # Increment SP
        self.assembly_instructions += [
            "D=A+1", 
            "@SP", 
            "M=D"
        ]


    # appends all the hack instructions required to get value at top of stack to be in register D
    def add_pop_value_from_stack_to_register_d_hack_assembly(self):
        # Decrement the SP
        self.assembly_instructions += [
            "@SP", 
            "A=M", 
            "D=A-1", 
            "@SP", 
            "M=D"
        ]

        # Store top of stack value into register D
        self.assembly_instructions += [
            "A=D", 
            "D=M"
        ]



    # returns the assembly instruction
    def get_assembly_instruction(self):
        return self.assembly_instructions


