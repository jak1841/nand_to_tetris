class vmWriter:
    def __init__(self):
        self.VM_commands_list = [] # Where the VM program will live
    
    # Segment = (constant, ARG, LCL, static, THIS, THAT, PTR, TEMP)

    # Writes VM push command
    def writePush(self, segment, index):
        self.VM_commands_list += [
            "push " + segment + " " + str(index)
        ]
    
    # Writes a VM pop command 
    def writePop(self, segment, index):
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
            return "multply"
        elif (op == "/"):
            return "division"
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