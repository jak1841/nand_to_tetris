"""
    This class is used to convert a file with hack cpu language to 
    its binary represetation cpu instruction  

    BASIC FORMAT 
    DEST=COMP;JUMP
"""
from arithemtic_logic_unit import alu
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
        self.comp_hashmap["D*A"] = "0" + "100001"   # Multiplication for fast computation
        self.comp_hashmap["D/A"] = "0" + "000001"   # Division for fast computation 

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
        self.comp_hashmap["D*M"] = "1" + "100001"   # Multiplication for fast computation
        self.comp_hashmap["D/M"] = "1" + "000001"   # Division for fast computation

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
        instruction = ""
        # A instruction 
        if (assembly_instruction[0] == "@"):
            result = list(str(bin(int(assembly_instruction[1:])))[2:])
            empty_instruction = ["0" for x in range(16)]
            for x in range(min(len(result), 15)):
                empty_instruction[-x - 1] = result[-x - 1]
            
            instruction = ''.join(empty_instruction)
        # C instruction
        else:
            # Tokenize the instruction 
            equal_index = assembly_instruction.find("=")
            semi_colon_index = assembly_instruction.find(";")


            dest_token = assembly_instruction[:equal_index]
            comp_token = assembly_instruction
            jump_token = assembly_instruction[semi_colon_index+1:]

            dest_binary = "000"
            jump_binary = "000"

            if (dest_token in self.dest_hashmap):
                dest_binary = self.dest_hashmap[dest_token]
                comp_token = comp_token[equal_index+1:]
            
            if (jump_token in self.jump_hashmap):
                semi_colon_index = comp_token.find(";")
                jump_binary = self.jump_hashmap[jump_token]
                comp_token = comp_token[:semi_colon_index]

            instruction = "111" + self.comp_hashmap[comp_token] + dest_binary + jump_binary
        return int(instruction.strip(), 2)

    # Input:        Array of Hack assembly instruction 
    # Output:       Array of binary instructions translated 
    def array_hack_assembly_instruction_to_binary_instruction(self, array_instructions):
        ret = []
        symbol_table = {}
        self.add_predefined_symbols_to_symbol_table(symbol_table)

        array_instructions = self.remove_comment_and_whitespace_from_array_assembly_instruction(array_instructions)

        a = alu()
        position = 0000000000000000
        # Does first pass which will get all the labels into symbol table 
        for x in array_instructions:
            # Label 
            if (x[0] == "(" and x[-1] == ")"):
                symbol = x[1:-1]
                symbol_table[symbol] = position
            # A or C instruction
            else:
                position = a.adder_16_bit(0x1, position)

            


        # Second pass which goes through and checks for every A instruction if symbol is in it, 
        # if it is then replace instruction with value in symbol table 
        # if not then a new symbol and add it to symbol table displacement
        
        symbol_table_displacement = 0b0000000000010000      # Where symbol table will be stored in memory
        for x in array_instructions:
            # Variable
            if (x[0] == "@" and x[1] not in "0123456789"):
                symbol = x[1:]
                if (symbol not in symbol_table):
                    symbol_table[symbol] = symbol_table_displacement
                    ret.append(symbol_table_displacement)
                    symbol_table_displacement = a.adder_16_bit(0x1, symbol_table_displacement)
                    
                else:
                    ret.append(symbol_table[symbol])

            # Label  
            elif (x[0] == "(" and x [-1] == ")"):
                pass
            else: 
                ret.append(self.hack_assembly_instruction_to_binary_instruction(x))
                
        return ret

    # Removes all lines of code that contain comments and empty whitespace from array
    def remove_comment_and_whitespace_from_array_assembly_instruction(self, array_instructions):
        ret = []
        for x in array_instructions:
            if (x == ""):
                pass
            elif (x[0] == "/" and x[1] == "/"):
                pass
            else:
                ret.append(x)
        
        return ret

    # Adds the predefined symbols to the given symbol table refering to the apporpiate positions in data memory
    def add_predefined_symbols_to_symbol_table(self, symboltable):
        symboltable["SP"] = 0000000000000000 
        symboltable["LCL"] = 0b0000000000000001 
        symboltable["ARG"] = 0b0000000000000010 
        symboltable["THIS"] = 0b0000000000000011 
        symboltable["THAT"] = 0b0000000000000100 

        symboltable["R0"] = 0b0000000000000000 
        symboltable["R1"] = 0b0000000000000001 
        symboltable["R2"] = 0b0000000000000010 
        symboltable["R3"] = 0b0000000000000011 
        symboltable["R4"] = 0b0000000000000100 
        symboltable["R5"] = 0b0000000000000101 
        symboltable["R6"] = 0b0000000000000110 
        symboltable["R7"] = 0b0000000000000111 
        symboltable["R8"] = 0b0000000000001000 
        symboltable["R9"] = 0b0000000000001001 
        symboltable["R10"] = 0b0000000000001010 
        symboltable["R11"] = 0b0000000000001011 
        symboltable["R12"] = 0b0000000000001100 
        symboltable["R13"] = 0b0000000000001101 
        symboltable["R14"] = 0b0000000000001110 
        symboltable["R15"] = 0b0000000000001111 

        symboltable["SCREEN"] = 0b0100000000000001 






   

        


        
