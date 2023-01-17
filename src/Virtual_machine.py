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
    
    Memory access VM commands:

         pop memorySegment index
         push memorySegment index

        Where memorySegment is static, this, local, argument, that, constant, pointer, or temp
        And index is a non-negative integer
     
        Static will be stored 16-255 
        local, argument, this, that will be stored in the heap (2048 - onward)
        but registers will be located at 1, 2, 3, 4 respectivivly

        The base addresses of these segments are kept in RAM
        addresses LCL, ARG, THIS, and THAT. Access to
        the i-th entry of any of these segments is
        implemented by accessing RAM[segmentBase + i]

        PTR, TEMP: 3-4 and 5-12 ram address respectively 
        They only edit the values at these locations
        

    

"""

class Vm:
    def __init__(self):
        self.assembly_instructions = []         # array will contain all the assembly instructions so far used in the project
        self.add_set_sp_hack_assembly()
        self.label_num = 0                      # Used to create unique labels to be used for comparison operations 
        self.return_num = 0                     # used to create unique function return labels
        self.add_init()
        self.current_function_scope = ""    # This will tell us which function we are currently in inside the vm_file
        # self.add_call_sys_init()

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
    
    # appends all hack instructions which call sys.init
    def add_init(self):
        # Sets base address initially so it doesnt overwrite sp 
        self.assembly_instructions += [
            "@2048",
            "D=A",
            "@LCL", 
            "M=D",
            "@2058", 
            "D=A",
            "@ARG", 
            "M=D", 
            "@2068", 
            "D=A",
            "@THIS", 
            "M=D", 
            "@2078", 
            "D=A",
            "@THAT", 
            "M=D", 
        ]
        

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
    def add_subtraction_hack_assembly(self):
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

    # appends all instructions which pops x, y from stack and pushes true if x < y else false 
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


    # appends all the hack instructions required to pop a value off the stack into the speceified memory segment
    # which will be in String format
        # "static" -> static 
        # "LCL" -> local 
        # "THIS" -> this 
        # "THAT" -> that 
        # "ARG" -> argument 
        # "temp" -> temp 
        # "ptr" -> pointer
    # into the given index
    def add_pop_value_from_stack_to_memory_segment_hack_instructions(self, instruction):
        instruction = instruction.split()
        index = int(instruction[2])
        memory_segment = instruction[1]

        

        if (memory_segment == "static"):
            self.add_pop_value_from_stack_to_register_d_hack_assembly()
            self.assembly_instructions+= [
            "@" + str(index + 16), 
            "M=D"
            ]
        elif (memory_segment in ["LCL", "THIS", "THAT", "ARG"]):
            # Store the address of where to store popped value from stack into R13
            self.assembly_instructions+= [
                "@" + memory_segment, 
                "D=M", 
                "@" + str(index), 
                "D=D+A",
                "@R13", 
                "M=D", 
            ]

            self.add_pop_value_from_stack_to_register_d_hack_assembly()

            self.assembly_instructions += [
                "@R13", 
                "A=M", 
                "M=D"
            ]
            
        elif (memory_segment == "PTR"):
            self.add_pop_value_from_stack_to_register_d_hack_assembly()
            self.assembly_instructions+= [
            "@" + str(3 + index), 
            "M=D"
            ]
        elif (memory_segment == "TEMP"):
            self.add_pop_value_from_stack_to_register_d_hack_assembly()
            self.assembly_instructions+= [
            "@" + str(5 + index), 
            "M=D"
            ]
        else:
            raise Exception("unknown memory segment", memory_segment)
        
    # appends all the hack instructions required to push a value from a speceficed memory segment and index 
    # to the stack 
        # "static" -> static 
        # "LCL" -> local 
        # "THIS" -> this 
        # "THAT" -> that 
        # "ARG" -> argument 
        # "temp" -> temp 
        # "ptr" -> pointer
    def add_push_memory_segment_to_stack_hack_instructions(self, vm_instruction):
        instruction = vm_instruction.split()
        index = int(instruction[2])
        memory_segment = instruction[1]

        if (memory_segment == "static"):
            self.assembly_instructions+= [
            "@" + str(index + 16), 
            "D=M"
            ]
            self.add_push_d_register_value_to_stack_hack_assembly()
        elif (memory_segment in ["LCL", "THIS", "THAT", "ARG"]):
            self.assembly_instructions+= [
                "@" + memory_segment, 
                "D=M", 
                "@" + str(index), 
                "D=D+A",
                "A=D",
                "D=M", 
            ]
            self.add_push_d_register_value_to_stack_hack_assembly()
        elif (memory_segment == "PTR"):
            self.assembly_instructions+= [
            "@" + str(3 + index), 
            "D=M"
            ]
            self.add_push_d_register_value_to_stack_hack_assembly()
        elif (memory_segment == "TEMP"):
            self.assembly_instructions+= [
            "@" + str(5 + index), 
            "D=M"
            ]
            self.add_push_d_register_value_to_stack_hack_assembly()
        else:
            raise Exception("Unexepected memory segment", memory_segment)


        
        
        
    """
      The purpose of the function_name_scope parameter is that labels have function level scopes so we are able 
      to use the same label name inside of different functions. We will have a variable to keep track of which 
      function we are currently writing VM instructions in. We will prepend this to label_name to create a unique 
      label name for that particular function scope. 

    """

    # VM instruction: label [label_name]
    def add_label_hack_assembly(self, vm_instruction):
        x = vm_instruction.split()
        Label_name = self.current_function_scope + ":" + x[1]
        self.assembly_instructions += ["(" + Label_name + ")"]

    # VM instruction: goto [label_name]
    def add_goto_label_hack_assembly(self, vm_instruction):
        x = vm_instruction.split()
        label_name = self.current_function_scope + ":" + x[1]
        self.assembly_instructions += [
        "@" + label_name,
        "0;JMP"
    ] 

    # if top of stack not zero, jump to the specified destination; otherwise, execute the next command in the program.
    # VM instruction: if-goto [label_name]	
    def add_if_goto_hack_assembly(self, vm_instruction):
        x = vm_instruction.split()
        label_name = self.current_function_scope + ":" + x[1]
        self.assembly_instructions += [
            "@SP", 
            "D=M-1", 
            "A=D", 
            "D=M", 
            "@" + label_name, 
            "D;JNE"
                ]


    # VM instruction: call f n
    # calling a function f after n arguments have been pushed onto the stack
    def add_call_function(self, vm_instruction):
        
        x = vm_instruction.split()
        function_name = x[1]
        n = x[2]
        return_address = "return_" + str(self.return_num)

        # PUSH RETURN ADDRESS
        self.assembly_instructions += [
            "@" + return_address, 
            "D=A"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

        # PUSH LCL
        self.assembly_instructions += [
            "@LCL", 
            "D=M"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

        # PUSH ARG
        self.assembly_instructions += [
            "@ARG", 
            "D=M"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

        # PUSH THIS
        self.assembly_instructions += [
            "@THIS", 
            "D=M"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()

        # PUSH THAT 
        self.assembly_instructions += [
            "@THAT", 
            "D=M"
        ]
        self.add_push_d_register_value_to_stack_hack_assembly()


        # ARG = SP - 5 - n
        # LCL = SP
        self.assembly_instructions += [
            "@SP", 
            "D=M", 
            "@LCL", 
            "M=D", 

            "@5", 
            "D=D-A", 
            "@" + str(n), 
            "D=D-A", 
            "@ARG", 
            "M=D",
        ]


        
        self.assembly_instructions += [
            "@" + function_name, 
            "0;JMP",
            "(" + return_address + ")"
        ]

        self.return_num+= 1

    # VM instruction: function f k 
    # where k is the number of local variables
    # local variables are initialized to 0 and added onto stack 
    def add_function_declaration_hack_assembly(self, vm_instruction):
        x = vm_instruction.split()
        function_name = x[1]
        num_local_variables = int(x[2])
        self.current_function_scope = function_name
        self.assembly_instructions += ["(" + function_name + ")"]
        
        for x in range(num_local_variables):
            self.add_push_constant_hack_assembly(0)
        
    # VM instruction: return
    # returns from a VM function
    # using the convention descirbed in the elements of computing machines book
    def add_return_hack_assembly(self, vm_instruction):
        # FRAME = LCL   // Frame is a temporary variable at location 7
        self.assembly_instructions += [
            "@LCL", 
            "D=M", 
            "@7",
            "M=D" 
        ]

        # RET = *(FRAME - 5)
        self.assembly_instructions += [
            "@7", 
            "D=M",
            "@5",
            "A=D-A",  
            "D=M", 
            "@8", 
            "M=D"
        ]

        # *ARG = pop()
        self.add_pop_value_from_stack_to_memory_segment_hack_instructions("pop ARG 0")

        # SP = ARG+1
        self.assembly_instructions += [
            "@ARG", 
            "D=M+1", 
            "@SP", 
            "M=D"
        ]

        # THAT = *(FRAME - 1)
        self.assembly_instructions += [
            "@7", 
            "D=M",
            "@1",
            "A=D-A",  
            "D=M",
            "@4", 
            "M=D" 
        ]

        # THIS = *(FRAME-2)
        self.assembly_instructions += [
            "@7", 
            "D=M",
            "@2",
            "A=D-A",  
            "D=M",
            "@3", 
            "M=D" 
        ]

        # ARG = *(FRAME - 3)
        self.assembly_instructions += [
            "@7", 
            "D=M",
            "@3",
            "A=D-A",  
            "D=M",
            "@2", 
            "M=D" 
        ]

        # LCL = *(FRAME - 4)
        self.assembly_instructions += [
            "@7", 
            "D=M",
            "@4",
            "A=D-A",  
            "D=M",
            "@1", 
            "M=D" 
        ]

        # GOTO RET
        self.assembly_instructions += [
            "@8", 
            "A=M", 
            "0;JMP"
        ]


    
    


    # returns the assembly instruction
    def get_assembly_instruction(self):
        return self.assembly_instructions

    # Given an array of VM instructions appends all instructions that are asscoiated with that particular VM instruction
    # to an array and returns the result
    def get_hack_assembly_instructions_from_VM_instructions(self, VM_instructions_array):
        # Clears array of assembly instructions
        self.assembly_instructions = []
        self.add_set_sp_hack_assembly()
        self.label_num = 0                      # Used to create unique labels to be used for comparison operations 
        self.return_num = 0                     # used to create unique function return labels
        self.add_init()
        self.current_function_scope = "" 

        for x in VM_instructions_array:
            if ("push constant " == x[:14]):
                number = int(x[14:])
                self.add_push_constant_hack_assembly(number)
            elif (x == "add"):
                self.add_addition_hack_assembly()
            elif (x == "sub"):
                self.add_subtraction_hack_assembly()
            elif (x == "neg"):
                self.add_negative_hack_assembly()
            elif (x == "eq"):
                self.add_equal_hack_assembly()
            elif (x == "gt"):
                self.add_greater_than_hack_assembly()
            elif (x == "lt"):
                self.add_less_than_hack_assembly()
            elif (x == "and"):
                self.add_and_hack_assembly()
            elif (x == "or"):
                self.add_or_hack_assembly()
            elif (x == "not"):
                self.add_not_hack_assembly()
            elif (x[:3] == "pop"):
                self.add_pop_value_from_stack_to_memory_segment_hack_instructions(x)
            elif (x[:4] == "push"):
                self.add_push_memory_segment_to_stack_hack_instructions(x)
            elif(x[:5] == "label"):
                self.add_label_hack_assembly(x)
            elif (x[:4] == "goto"):
                self.add_goto_label_hack_assembly(x)
            elif (x[:7] == "if-goto"):
                self.add_if_goto_hack_assembly(x)
            elif (x[:6] == "return"):
                self.add_return_hack_assembly(x)
            elif (x[:4] == "call"):
                self.add_call_function(x)
            elif (x[:8] == "function"):
                self.add_function_declaration_hack_assembly(x)
            else:
                raise Exception("Unexpected VM instruction:", x)
        
        
        return self.get_assembly_instruction()


    
        

