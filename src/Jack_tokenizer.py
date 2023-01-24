class tokenizer:
    def __init__(self, jack_program_string):
        self.jack_program_string = jack_program_string
        self.cur_index = 0  # Gets the current index inside the jack_program



    # Checks to see if the current position in the program will lead to a symbol token
    def is_symbol_token(self):
        symbol = self.jack_program_string[self.cur_index]

        return symbol in ["{", "}", "(", ")", "[", "]", ".", ';', ",", "+", "-", "*", "/", "&", "|", "<", ">", "="]
        
    # Assuming cur position leads to a symbol token returns that token
    def get_symbol_token(self):
        self.cur_index += 1
        return (self.jack_program_string[self.cur_index-1], "symbol")


    # checks to see if the current position in the program will lead to a integerConstant token
    def is_integer_constant_token(self):
        return self.jack_program_string[self.cur_index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Assuming cur position leads to a integer_constant return that token
    def get_integer_constant_token(self):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        cur_symbol = self.jack_program_string[self.cur_index]
        ret = ""
        while (self.is_EOF() == False and cur_symbol in numbers):
            ret += cur_symbol
            self.cur_index += 1
            cur_symbol = self.jack_program_string[self.cur_index]

        return (ret, "integerConstant")

    # checks to see if the current position in the program will lead to a stringConstant token
    def is_stringConstant_token(self):
        return self.jack_program_string[self.cur_index] == "\""

    # assuming current token leads to a stringConstant token return that token 
    def get_stringConstant_token(self):
        self.cur_index += 1
        cur_symbol = self.jack_program_string[self.cur_index]
        ret = ""
        try:
            while (cur_symbol != "\""):
                ret += cur_symbol
                self.cur_index += 1
                cur_symbol = self.jack_program_string[self.cur_index]
        except:
            raise Exception("StringConstant_token error EOF reached\n No \" found")
        
        self.cur_index += 1
        return (ret, "stringConstant")
        
    # checks to see if the current position in the program will lead to a identifier       
    # identifier is a sequence of letters, digits, and underscore that does not start with a digit
    def is_identifier_token(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  
        underscore = "_"
        cur_char = self.jack_program_string[self.cur_index]
        return cur_char in letters or cur_char in underscore
    
    # assuming current token leads to identifier token return that specefic token
    def get_identifier_token(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  
        underscore = "_"
        numbers = "0123456789"
        acceptable_characters = letters + underscore + numbers
        
        ret = ""

        cur_char = self.jack_program_string[self.cur_index]

        while (self.is_EOF() == False and cur_char.isspace() == False and cur_char in acceptable_characters):
            ret += cur_char
            self.cur_index+= 1
            cur_char = self.jack_program_string[self.cur_index]
        
        return (ret, "identifier")


    # given a string if it is the case that it is a keyword
    def is_key_word(self, string):
        return (string in ["class", "constructor", "function", "method",
        "field", "static", "var", "int", "char", "boolean", "void", 
        "true", "false", "null", "this", "let", "do", "if", "else", 
        "while", "return"])

    # returns list of tokens in jack program
    def get_all_tokens(self):
        token_list = []
        while (self.is_EOF() == False):
            token_list.append(self.get_next_token())
        
        if (token_list[-1] == None):
            return token_list[:-1]
        return token_list

    # returns list of all tokens in fxml format
    def print_all_tokens_fxml(self):
        ret = "<tokens>\n"
        for x in self.get_all_tokens():
            if (x[1] == "keyword"):
                ret += " <keyword> " + x[0] + " </keyword>\n"
            elif (x[1] == "symbol"):
                ret += " <symbol> " + x[0] + " </symbol>\n"
            elif (x[1] == "identifier"):
                ret += " <identifier> " + x[0] + " </identifier>\n"
            elif (x[1] == "integerConstant"):
                ret += " <integerConstant> " + x[0] + " </integerConstant>\n"
            elif (x[1] == "stringConstant"):
                ret += " <stringConstant> " + x[0] + " </stringConstant>\n"
            else:
                raise Exception("unknown token")
        
        ret += "</tokens>"
        print(ret)
            


    # returns the enxt token and advances the current position in the array
    def get_next_token(self):
        self.remove_whitespace()

        if (self.is_EOF() == False):
            if (self.is_symbol_token()):
                return self.get_symbol_token()
            elif (self.is_integer_constant_token()):
                return self.get_integer_constant_token()
            elif (self.is_stringConstant_token()):
                return self.get_stringConstant_token()
            elif (self.is_identifier_token()):
                ident_token = self.get_identifier_token()
                if (self.is_key_word(ident_token[0])):
                    return (ident_token[0], "keyword")
                return ident_token
            else:
                raise Exception("unknown token", self.jack_program_string[self.cur_index:])
        


    
    def is_EOF(self):
        return self.cur_index >= len(self.jack_program_string)

    # Removes whitespace from the jack_program if encountered
    def remove_whitespace(self):
        while (self.is_EOF() == False and self.jack_program_string[self.cur_index].isspace()):
            self.cur_index += 1

