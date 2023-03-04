class vmWriter:
    def __init__(self):
        self.VM_commands_list = [] # Where the VM program will live

        # initialize it with sys.init calling main and then forever looping 
        self.initialize_call_main()
    
    def initialize_call_main(self):
        self.VM_commands_list += [
            "function sys.init 0", 
            "call Main_Classmain 0", 
            "label end", 
            "goto end",
        ]
        

    def initialize_memory_class (self):
        jack_memory_class = """
            class Memory {
                static int ram; 
                static int heap_base;

                /* Called in sys.init function always*/
                function void init() {
                    let heap_base = 2048;
                    let ram = 0;
                    return 0;
                }

                /*  Get value at that address in RAM */
                function int peek(int address) {
                    return ram[address];
                }

                /* Update value at given address with given value in RAM */
                function void poke(int address, int value) {
                    let ram[address] = value;
                    return 0;
                }

                /* Allocates n different memory position */
                function int alloc(int n) {
                    var int block; 
                    let block = heap_base;
                    let heap_base = heap_base + n;
                    return block;
                }

                /* Deallocates a object given its pointer*/
                function void deAlloc (int object_address) {
                    return 0;
                }
            }

        """
    

        



    # Segment = (constant, ARG, LCL, static, THIS, THAT, PTR, TEMP)

    # Given a segment thats eithier VAR, FIELD, static, method 
    # returns the correct on associated with it 
    def translate_segment_to_VM_segment(self, segment):
        if (segment == "VAR"):
            return "LCL"
        elif (segment == "STATIC"):
            return "static"
        elif (segment == "FIELD"):
            return "ARG"
        
        return segment

    # Writes VM push command
    def writePush(self, segment, index):
        segment = self.translate_segment_to_VM_segment(segment)
        
        self.VM_commands_list += [
            "push " + segment + " " + str(index)
        ]
    
    # Writes a VM pop command 
    def writePop(self, segment, index):
        segment = self.translate_segment_to_VM_segment(segment)
        
        self.VM_commands_list += [
            "pop " + segment + " " + str(index)
        ]
    
    # Command = (add, sub, neg, eq, gt, lt, and, or, not)
    # Writes arithmetic command 
    def writeArithmetic(self, command):
        command = self.get_arithemetic_command_from_op(command)
        self.VM_commands_list += [command]
    
    def get_arithemetic_command_from_op (self, op):
        if (op == "+"):
            return "add"
        elif (op == "-"):
            return "sub"
        elif (op == "*"):
            return "mult"
        elif (op == "/"):
            return "div"
        elif (op == "&"):
            return "and"
        elif (op == "|"):
            return "or"
        elif (op == "<"):
            return "lt"
        elif (op == ">"):
            return "gt"
        elif (op == "="):
            return "eq"
        elif (op == "neg"):
            return "neg"
        elif (op == "not"):
            return "not"

    
    # Writes a VM labeled command
    def writeLabel(self, label_name):
        self.VM_commands_list += [
            "label " + label_name 
        ]
    
    # Writes a VM goto command
    def writeGoto (self, label_name):
        self.VM_commands_list += [
            "goto " + label_name
        ]


    
    
    # Writes a VM if-goto command 
    def writeIfGoto (self, label_name):
        self.VM_commands_list += [
            "if-goto " + label_name
        ]

    # Writes a VM call command 
    def writeCall (self, name, num_args):
        
        self.VM_commands_list += [
            "call " + name + " " + str(num_args)
        ]

    # Writes a VM Function command 
    def writeFunction (self, name, num_locals):
        self.VM_commands_list += [
            "function " + name + " " + str(num_locals)
        ]
    
    # Writes VM return command 
    def writeReturn (self):
        self.VM_commands_list += [
            "return"
        ]