
# Given a jack program will compile the class and produce and output
# The Grammar is defined on Page 246 in elements of computing systems. 
from Jack_tokenizer import tokenizer as tk
class comp_engine:
    def __init__(self, jack_program_string):
        self.tokens = tk(jack_program_string).get_all_tokens()
        


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
                return
            else:
                raise Exception("Type not matching", token)

    # Given a symbol will check that the symbol matches and advances to the next token
    # Does error checking as well if symbol does not match
    def match_token_symbol(self, symbol):
        token = self.tokens.pop(0)

        if (token[0] == symbol):
            return
        
        raise Exception("Expected symbol", symbol, "But got", token)

    def match_class(self):
        self.match_token_symbol("class")
        self.match_class_Name()
        self.match_token_symbol("{")

        # classVarDec*
        while (self.tokens[0][0] in ["static", "field"]):
            self.match_classVarDec()
        
        # subroutineDec*
        while (self.tokens[0][0] in ["constructor", "function", "method"]):
            self.match_subroutineDec()


        self.match_token_symbol("}")

    def match_classVarDec(self):
        if (self.tokens[0][0] == "static"):
            self.match_token_symbol("static")
        else:
            self.match_token_symbol("field")

        
        self.match_type()
        self.match_varName()

        # will be able to declare multiple variables in same line. 
        # type var1, var2
        
        while (self.tokens[0][0] == ","):
            self.match_token_symbol(",")
            self.match_varName()


        self.match_token_symbol(";")
        
    def match_subroutineDec(self):
        token = self.tokens.pop(0)
        if (token[0] not in ["constructor", "function", "method"]):
            raise Exception("Expected constructor, function, method but got", token)
        
        token = self.tokens[0][0]
        if (token == "void"):
            self.tokens.pop(0)
        else:
            self.match_type()
        
        self.match_subroutine_Name()
        self.match_token_symbol("(")

        # parameter list
        self.match_parameter_list()

        self.match_token_symbol(")")
        self.match_subroutineBody()
    
    def match_subroutineBody(self):
        self.match_token_symbol("{")

        while (self.tokens[0][0] == "var"):
            self.match_varDec()
        
        self.match_statements()

        self.match_token_symbol("}")

    def match_parameter_list(self):
        if (self.is_type_token()):
            self.match_type()
            self.match_varName()
        
        while (self.tokens[0][0] == ","):
            self.match_token_symbol(",")
            self.match_type()
            self.match_varName()


        

    def match_class_Name(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return
        else:
            raise Exception("className not matching", token)
    
    def match_subroutine_Name(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return
        else:
            raise Exception("subroutineName not matching", token)
    
    def match_varName(self):
        token = self.tokens.pop(0)
        if (token[1] == "identifier"):
            return
        else:
            raise Exception("varName not matching", token)
        
    def match_varDec(self):
        self.match_token_symbol("var")

        self.match_type()
        self.match_varName()
        
        while (self.tokens[0][0] == ","):
            self.match_token_symbol(",")
            self.match_varName()
        
        self.match_token_symbol(";")

        
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

    def match_let_statement(self):
        self.match_token_symbol("let")
        self.match_varName()

        # ( '[' Expression ']' )?
        self.match_token_symbol("=")
        # Expression 
        self.match_token_symbol(";")
    
    def match_if_statement(self):
        self.match_token_symbol("if")
        self.match_token_symbol("(")
        # Expression
        self.match_token_symbol(")")
        self.match_token_symbol("{")

        self.match_statements()

        self.match_token_symbol("}")

        if (self.tokens[0][0] == "else"):
            self.match_token_symbol("else")
            self.match_token_symbol("{")
            self.match_statements()
            self.match_token_symbol("}")
            
    def match_while_statement(self):
        self.match_token_symbol("while")
        self.match_token_symbol("(")

        # Expression

        self.match_token_symbol(")")
        self.match_token_symbol("{")
        
        self.match_statements()
        self.match_token_symbol("}")

    def match_do_statement(self):
        self.match_token_symbol("do")

        # Subroutine call

        self.match_token_symbol(";")

    def match_return_statement(self):
        self.match_token_symbol("return")
        
        # Expression ?

        self.match_token_symbol(";")
            

    
