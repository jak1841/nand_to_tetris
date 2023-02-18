
# Given a jack program will compile the class and produce and output
# The Grammar is defined on Page 246 in elements of computing systems. 
from Jack_tokenizer import tokenizer as tk
from Jack_symbol_table import symbol_table
from vm_writer import vmWriter
from collections import defaultdict

class comp_engine:
    def __init__(self, jack_program_string):
        self.tokens = tk(jack_program_string).get_all_tokens()
        self.symbol_table = symbol_table()
        self.vm_program = vmWriter()
        self.label_index = 0    # Used to create a unique label name for if, else, while, etc
        self.current_class_name = ""    # Assuming multiple classes will return the current class name
        self.number_fields_current_class = 0

        self.map_class_names_to_function_names = defaultdict(list)         # name_class -> list of function names



    # This function will add all the libraries to tokens list
    def add_all_libraries_to_tokens(self):
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
        self.tokens += tk(jack_memory_class).get_all_tokens()

        


    """ 
    
        PROGRAM STRUCTURE GRAMMAR RULES AND FUNCTIONS BELOW

    """
    
    # Returns true if the current token is a type 
    def is_type_token(self):
        token = self.tokens[0]
        if (token[0] in ["int", "char", "boolean"] or token[1] == "identifier"):
            return True
        return False

    # Assuming the tokens should be a type confirms this and advances the tokens counter
    def match_type(self):
            token = self.tokens.pop(0)
            if (token[0] in ["int", "char", "boolean"] or token[1] == "identifier"):
                return token[0]
            else:
                raise Exception("Type not matching", token)

    # Given a symbol will check that the symbol matches and advances to the next token
    # Does error checking as well if symbol does not match
    def match_token_symbol(self, symbol):
        token = self.tokens.pop(0)
        if (token[0] == symbol):
            return token
        raise Exception("Expected symbol", symbol, "But got", token, self.tokens)

    def match_class(self):
        self.match_token_symbol("class")
        self.current_class_name = self.match_class_Name()
        self.number_fields_current_class = 0
        self.match_token_symbol("{")

        # classVarDec*
        while (self.tokens[0][0] in ["static", "field"]):
            self.match_classVarDec()
        
        # subroutineDec*
        while (self.tokens[0][0] in ["constructor", "function", "method"]):
            self.match_subroutineDec()


        self.match_token_symbol("}")

    def match_classVarDec(self):

        kind = "STATIC"
        if (self.tokens[0][0] == "static"):
            self.match_token_symbol("static")
        else:
            self.match_token_symbol("field")
            self.number_fields_current_class += 1
            kind = "FIELD"

        
        type_variable = self.match_type()
        name_variable = self.match_varName()

        self.symbol_table.define_new_identifier(name_variable, type_variable, kind)
        

        # will be able to declare multiple variables in same line. 
        # type var1, var2
        
        while (self.tokens[0][0] == ","):
            self.match_token_symbol(",")
            name_variable = self.match_varName()
            self.symbol_table.define_new_identifier(name_variable, type_variable, kind)

            # Counts the number of field variables
            if (kind == "FIELD"):
                self.number_fields_current_class += 1


        self.match_token_symbol(";")
        
    def match_subroutineDec(self):
        token = self.tokens.pop(0)
        function_type = token[0]
        if (token[0] not in ["constructor", "function", "method"]):
            raise Exception("Expected constructor, function, method but got", token)
        
        
        token = self.tokens[0][0]
        function_return_type = token
        if (token == "void"):
            self.tokens.pop(0)
        else:
            self.match_type()
        
        function_name = self.match_subroutine_Name()
        self.map_class_names_to_function_names[self.current_class_name].append(function_name)

        self.match_token_symbol("(")

        self.symbol_table.clear_subroutine_symbol_table()

        # parameter list
        num_args = self.match_parameter_list()

        self.match_token_symbol(")")

        

        self.match_subroutineBody(function_name, function_type, function_return_type)
    
    def match_subroutineBody(self, function_name, function_type, function_return_type):
        self.match_token_symbol("{")

        num_local_variables = 0
        while (self.tokens[0][0] == "var"):
            num_local_variables += 1
            self.match_varDec()
        

        
        self.vm_program.writeFunction(str(self.current_class_name) + function_name, num_local_variables)
        
        if (function_type == "constructor"):
            self.match_constructor_def()

        
        self.match_statements()

        self.match_token_symbol("}")

    # Matches parameter list and returns the number of ARGS
    def match_parameter_list(self):
        type_variable = None
        name_variable = None
        num_args = 0    
        if (self.is_type_token()):
            type_variable = self.match_type()
            name_variable = self.match_varName()
            self.symbol_table.define_new_identifier(name_variable, type_variable, "ARG")
            num_args += 1
        
            while (self.tokens[0][0] == ","):
                self.match_token_symbol(",")
                type_variable = self.match_type()
                name_variable = self.match_varName()
                self.symbol_table.define_new_identifier(name_variable, type_variable, "ARG")
                num_args+= 1
        
        return num_args

    def match_class_Name(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return token[0]
        else:
            raise Exception("className not matching", token)
    
    def match_subroutine_Name(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return token[0]
        else:
            raise Exception("subroutineName not matching", self.tokens)
    
    def match_varName(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return token[0]
        else:
            raise Exception("varName not matching", token)
        
    def match_varDec(self):
        self.match_token_symbol("var")

        type_variable = self.match_type()
        name_variable = self.match_varName()
        self.symbol_table.define_new_identifier(name_variable, type_variable, "VAR")

        
        while (self.tokens[0][0] == ","):
            self.match_token_symbol(",")
            name_variable = self.match_varName()
            self.symbol_table.define_new_identifier(name_variable, type_variable, "VAR")

        
        self.match_token_symbol(";")

    # Given a function name will add constructor code for vm
    def match_constructor_def(self):  
        
        self.vm_program.writePush("constant", self.number_fields_current_class)
        self.vm_program.writeCall("Memoryalloc", 1) 
        self.vm_program.writePop("PTR", 0) # Stored in the this pointer

        
    
    """
    
        STATEMENTS GRAMMAR RULES AND FUNCTIONS BELOW
    
    """
    # Given current token will return true if it leads to a statement 
    def is_statement(self):
        cur_symbol = self.tokens[0][0]

        return (cur_symbol in ["let", "if", "while", "do", "return"])

    def match_statements(self):
        while (self.is_statement()):
            self.match_statement()

    def match_statement(self):
        cur_symbol = self.tokens[0][0]
        if (cur_symbol == "let"):
            self.match_let_statement()
        elif (cur_symbol == "if"):
            self.match_if_statement()
        elif (cur_symbol == "while"):
            self.match_while_statement()
        elif (cur_symbol == "do"):
            self.match_do_statement()
        elif (cur_symbol == "return"):
            self.match_return_statement()
        else:
            raise Exception("Token not leading to statement", cur_symbol)

    def match_field_let_statement(self, identifier_assigned):
        # ASSUMING THIS has the correct pointer to the object 
        self.match_token_symbol("=")
        self.match_expression() 
        self.match_token_symbol(";")

        self.vm_program.writePop("THIS", self.symbol_table.index_of(identifier_assigned))





    def match_let_statement(self):
        self.match_token_symbol("let")
        identifier_assigned = self.match_varName()

        if (self.symbol_table.kind_of(identifier_assigned) == "FIELD"):
            self.match_field_let_statement(identifier_assigned)

        elif (self.tokens[0][0] == "["):
            self.vm_program.writePush(self.symbol_table.kind_of(identifier_assigned), self.symbol_table.index_of(identifier_assigned))
            self.match_token_symbol("[")
            self.match_expression()
            self.match_token_symbol("]")

            self.vm_program.writeArithmetic("+")
            self.vm_program.writePop("PTR", 1)
            self.match_token_symbol("=")
            self.match_expression() 
            self.match_token_symbol(";") 
            self.vm_program.writePop("THAT", 0)
        
        else:
            self.match_token_symbol("=")
            self.match_expression() 
            self.match_token_symbol(";")

            self.vm_program.writePop(self.symbol_table.kind_of(identifier_assigned), self.symbol_table.index_of(identifier_assigned))
    
    def match_if_statement(self):
        self.match_token_symbol("if")
        self.match_token_symbol("(")
        
        self.match_expression() # Conditionitional 
        # makes negative 
        self.vm_program.writeArithmetic("not")
        self.vm_program.writeIfGoto("L" + str(self.label_index))    # Depending on truth value of conditonal



        self.match_token_symbol(")")
        self.match_token_symbol("{")

        self.match_statements()

        self.vm_program.writeGoto("L" + str(self.label_index + 1))  # jumping past else

        self.match_token_symbol("}")

        if (self.tokens[0][0] == "else"):
            self.match_token_symbol("else")
            self.match_token_symbol("{")
            self.vm_program.writeLabel("L" + str(self.label_index))
            self.match_statements()
            self.match_token_symbol("}")
        
        self.vm_program.writeLabel("L" + str(self.label_index + 1))
        self.label_index += 2
            
    def match_while_statement(self):
        self.match_token_symbol("while")
        self.match_token_symbol("(")

        self.vm_program.writeLabel("L" + str(self.label_index))
        self.match_expression() # Conditional 
        # get the not of the conditional 
        self.vm_program.writeArithmetic("not")
        self.vm_program.writeIfGoto("L" + str(self.label_index + 1))

        self.match_token_symbol(")")
        self.match_token_symbol("{")
        
        self.match_statements()
        self.vm_program.writeGoto("L" + str(self.label_index))
        self.vm_program.writeLabel("L" + str(self.label_index + 1))
        self.label_index += 2
        self.match_token_symbol("}")

    def match_do_statement(self):
        self.match_token_symbol("do")

        self.match_subroutine_call()

        self.match_token_symbol(";")

    def match_return_statement(self):
        self.match_token_symbol("return")
        
        if (self.tokens[0][0] != ";"):
            self.match_expression()
        
        self.vm_program.writeReturn()
        
        self.match_token_symbol(";")
            

    """
    
        EXPRESSIONS GRAMMAR RULES AND FUNCTIONS BELOW
    

    """
    # returns true if the current token is a keyword constant
    def is_keywordConstant(self):
        cur_symbol = self.tokens[0][0]
        return cur_symbol in ["true", "false", "this", "null"]

    def match_expression(self):
        self.match_term()

        while (self.is_op()):
            op = self.match_op()
            self.match_term()
            self.vm_program.writeArithmetic(op)


    # Given a field from a certain object pushes that field value onto stack 
    def add_field_to_stack(self, identifier_name):
        # Assumes PTR 0 or this pointer has current object 
        self.vm_program.writePush("THIS", self.symbol_table.index_of(identifier_name))
        
        

    def match_term (self):
        cur_token_type = self.tokens[0][1]
        cur_token_symbol = self.tokens[0][0]

        if (cur_token_type == "integerConstant"):
            self.tokens.pop(0)
            self.vm_program.writePush("constant", str(cur_token_symbol))
        elif (cur_token_type == "stringConstant"):
            self.tokens.pop(0)
        elif (self.is_keywordConstant()):
            self.match_key_word_constant()
        # VarName [expression]
        elif (cur_token_type == "identifier" and self.tokens[1][0] == "["):
            var_name = self.match_varName()
            self.vm_program.writePush(self.symbol_table.kind_of(var_name), self.symbol_table.index_of(var_name))
            self.match_token_symbol("[")
            self.match_expression()
            self.match_token_symbol("]")
            self.vm_program.writeArithmetic("+")
            self.vm_program.writePop("PTR", 1)
            self.vm_program.writePush("THAT", 0)
        # subroutine_call 
        elif (cur_token_type == "identifier" and (self.tokens[1][0] == "(" or self.tokens[1][0] == ".")):
            self.match_subroutine_call()
        # varName
        elif (cur_token_type == "identifier"):
            self.match_varName()
            if (self.symbol_table.kind_of(cur_token_symbol) == "FIELD"):
                self.add_field_to_stack(cur_token_symbol)
            else:
                self.vm_program.writePush(self.symbol_table.kind_of(cur_token_symbol), self.symbol_table.index_of(cur_token_symbol))
        # "(" Expression ")"
        elif (cur_token_symbol == "("):
            self.match_token_symbol("(")

            self.match_expression() 

            self.match_token_symbol(")")
    
        else:
            self.match_unaryOp()
            self.match_term()
            self.vm_program.writeArithmetic("neg")


    def match_expression_list(self):
        
        num_args = 0
        if (self.tokens[0][0] != ")"):
            self.match_expression()
            num_args += 1
            while (self.tokens[0][0] == ","):
                self.tokens.pop(0)
                self.match_expression()
                num_args += 1
        
        return num_args
        
        
    def match_subroutine_call (self):
        subroutine_name = ""
        num_args = 0
        # Function calling not with object
        if (self.tokens[1][0] == "("):
            subroutine_name = self.match_subroutine_Name()
            self.match_token_symbol("(")
            num_args = self.match_expression_list() 
            self.match_token_symbol(")")
        elif (self.tokens[0][1] == "identifier"):
            identifier_name = self.tokens.pop(0)[0]
            self.match_token_symbol(".")
            
            # call function with created object
            if (self.symbol_table.is_identifier_in_symbol_table(identifier_name)):
                subroutine_name = self.symbol_table.type_of(identifier_name) + self.match_subroutine_Name()

                self.vm_program.writePush("PTR", 0)
                self.vm_program.writePop("TEMP", 6)

                self.vm_program.writePush(self.symbol_table.kind_of(identifier_name), self.symbol_table.index_of(identifier_name)) # pushes object which acts like data encapsulation
                self.vm_program.writePop("PTR", 0)
                self.match_token_symbol("(")
                num_args += self.match_expression_list()
                self.match_token_symbol(")")
        
                self.vm_program.writeCall(subroutine_name, num_args)
                self.vm_program.writePush("TEMP", 6)
                self.vm_program.writePop("PTR", 0)
                
                
                
            # call function statically
            else:
                subroutine_name = self.match_subroutine_Name()
                subroutine_name = identifier_name + subroutine_name

                self.match_token_symbol("(")
                num_args += self.match_expression_list()  
                self.match_token_symbol(")")
        
                self.vm_program.writeCall(subroutine_name, num_args)

    # Returns true if the current token is an op
    def is_op(self):
        cur_symbol = self.tokens[0][0]
        return (cur_symbol in "+-*/&|<>=")

    # Returns true subroutine name is in class

    def match_op(self):
        cur_symbol = self.tokens[0][0]
        if (cur_symbol == "+"):
            self.match_token_symbol("+")
        elif (cur_symbol == "-"):
            self.match_token_symbol("-")
        elif (cur_symbol == "*"):
            self.match_token_symbol("*")
        elif (cur_symbol == "/"):
            self.match_token_symbol("/")
        elif (cur_symbol == "&"):
            self.match_token_symbol("&")
        elif (cur_symbol == "|"):
            self.match_token_symbol("|")
        elif (cur_symbol == "<"):
            self.match_token_symbol("<")
        elif (cur_symbol == ">"):
            self.match_token_symbol(">")
        elif (cur_symbol == "="):
            self.match_token_symbol("=")
        else:
            raise Exception("unknown operator", cur_symbol)
        
        return cur_symbol
        
    def match_unaryOp(self):
        self.match_token_symbol("-")

    def match_key_word_constant (self):
        cur_symbol = self.tokens[0][0]

        # true = -1 
        # false = 0
        # null = 0
        # this = PTR 0

        if (cur_symbol == "true"):
            self.match_token_symbol("true")
            self.vm_program.writePush("constant", "1")
            self.vm_program.writeArithmetic("neg")
        elif (cur_symbol == "false"):
            self.match_token_symbol("false")
            self.vm_program.writePush("constant", "0")
        elif (cur_symbol == "null"):
            self.match_token_symbol("null")
            self.vm_program.writePush("constant", "0")
        elif (cur_symbol == "this"):
            self.match_token_symbol("this")
            self.vm_program.writePush("PTR", "0")
        else:
            raise Exception("Unknown Keyword Constant")
        
    def match_jack_program(self):
        while (len(self.tokens) > 0 and self.tokens[0][0] == "class"):
            self.match_class()
        

