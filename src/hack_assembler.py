"""
    This class is used to convert a file with hack cpu language to 
    its binary represetation cpu instruction  
"""
class assembler:
    def __init__(self):
        self.init_comp_hashmap()
        self.init_dest_hashmap()
        self.init_jump_hashmap()
        

    # Makes an hashmap which maps a symbol computation to its 
    # binary representation prepended with a bit
    def init_comp_hashmap(self):
        self.comp_hashmap = {}

        # A = 0
        self.comp_hashmap["0"] = "0101010"
        self.comp_hashmap["1"] = "0111111"
        self.comp_hashmap["-1"] = "0111010"
        self.comp_hashmap["D"] = "0001100"
        self.comp_hashmap["A"] = "0110000"
        self.comp_hashmap["!D"] = "0001101"
        self.comp_hashmap["!A"] = "0110001"
        self.comp_hashmap["-D"] = "0001111"
        self.comp_hashmap["-A"] = "0" + "110011"
        self.comp_hashmap["D+1"] = "0" + "011111"
        self.comp_hashmap["A+1"] = "0" + "110111"
        self.comp_hashmap["D-1"] = "0" + "001110"
        self.comp_hashmap["A-1"] = "0" + "110010"
        self.comp_hashmap["D+A"] = "0" + "000010"
        self.comp_hashmap["D-A"] = "0" + "010011"
        self.comp_hashmap["A-D"] = "0" + "000111"
        self.comp_hashmap["D&A"] = "0" + "000000"
        self.comp_hashmap["D|A"] = "0" + "010101"

        # A = 1
        self.comp_hashmap["M"] = "1" + "110000"
        self.comp_hashmap["!M"] = "1" + "110001"
        self.comp_hashmap["-M"] = "1" + "110011"
        self.comp_hashmap["M+1"] = "1" + "110111"
        self.comp_hashmap["M-1"] = "1" + "110010"
        self.comp_hashmap["D+M"] = "1" + "000010"
        self.comp_hashmap["D-M"] = "1" + "010011"
        self.comp_hashmap["M-D"] = "1" + "000111"
        self.comp_hashmap["D&M"] = "1" + "000000"
        self.comp_hashmap["D|M"] = "1" + "010101"

    # makes an hashmap which maps symbol dest to its 
    # binary representation
    def init_dest_hashmap(self):
        self.dest_hashmap = {}
        
        self.dest_hashmap["null"] = "000"
        self.dest_hashmap["M"] = "001"
        self.dest_hashmap["D"] = "010"
        self.dest_hashmap["MD"] = "011"
        self.dest_hashmap["A"] = "100"
        self.dest_hashmap["AM"] = "101"
        self.dest_hashmap["AD"] = "110"
        self.dest_hashmap["AMD"] = "111"


    # Makes an hashmap which maps symbols jump to its binary representation 
    def init_jump_hashmap(self):
        self.jump_hashmap = {}
        self.jump_hashmap["null"] = "000"
        self.jump_hashmap["JGT"] = "001"
        self.jump_hashmap["JEQ"] = "010"
        self.jump_hashmap["JGE"] = "011"
        self.jump_hashmap["JLT"] = "100"
        self.jump_hashmap["JNE"] = "101"
        self.jump_hashmap["JLE"] = "110"
        self.jump_hashmap["JMP"] = "111"

    # Input:        Hack assembly instruction 
    # Output:       binary instruction 
    def hack_assembly_instruction_to_binary_instruction(self, assembly_instruction):
        # A instruction 
        if (assembly_instruction[0] == "@"):
            result = list(str(bin(int(assembly_instruction[1:])))[2:])
            empty_instruction = ["0" for x in range(16)]
            for x in range(min(len(result), 15)):
                empty_instruction[-x - 1] = result[-x - 1]
            
            return ''.join(empty_instruction)
        # C instruction
        else:
            # Tokenize the instruction 
            equal_index = assembly_instruction.find("=")
            semi_colon_index = assembly_instruction.find(";")

            dest_token = assembly_instruction[:equal_index]
            comp_token = assembly_instruction[equal_index + 1: semi_colon_index]
            jump_token = assembly_instruction[semi_colon_index+1:]
            return "111" + self.comp_hashmap[comp_token] + self.dest_hashmap[dest_token] + self.jump_hashmap[jump_token]

             


        
