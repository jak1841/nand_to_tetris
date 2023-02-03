class symbol_table:
    def __init__(self):
        self.class_symbol_table = {}
        self.subroutine_symbol_table = {}
        self.running_index_class = 0
        self.running_index_subroutine = 0

    
    # Resets the subroutine symbol table
    def clear_subroutine_symbol_table(self):
        self.subroutine_symbol_table.clear()
        self.running_index_subroutine = 0
    
    # Creates a new identifieir and adds it to corresponding symbol table
    # where name is name of identifier 
    # type is type of identifier 
    # kind is eithier (STATIC, FIELD, ARG, VAR)
    # STATIC, FIELD is class scope 
    # ARG and VAR is subroutine scope
    # (TYPE, KIND, INDEX)
    def define_new_identifier(self, name, type, kind):
        if (kind in ["STATIC", "FIELD"]):
            self.class_symbol_table[name] = (type, kind, self.running_index_class)
            self.running_index_class += 1
        elif (kind in ["ARG", "VAR"]):
            self.subroutine_symbol_table[name] = (type, kind, self.running_index_subroutine)
            self.running_index_subroutine += 1
        
        else:
            raise Exception("Unknown kind", kind)


    # Given name of identifier in current scope returns its kind 
    def kind_of(self, name):
        if (name in self.subroutine_symbol_table):
            return self.subroutine_symbol_table[name][1]
        elif (name in self.class_symbol_table):
            return self.class_symbol_table[name][1]
        else:
            raise Exception("unknown identifier name", name)

    # Given name of identifier in current scope returns its type
    def type_of(self, name):
        if (name in self.subroutine_symbol_table):
            return self.subroutine_symbol_table[name][0]
        elif (name in self.class_symbol_table):
            return self.class_symbol_table[name][0]
        else:
            raise Exception("unknown identifier name", name)

    # Given name of identifier in current scope returns its index 
    def index_of(self, name):
        if (name in self.subroutine_symbol_table):
            return self.subroutine_symbol_table[name][2]
        elif (name in self.class_symbol_table):
            return self.class_symbol_table[name][2]
        else:
            raise Exception("unknown identifier name", name)





    

