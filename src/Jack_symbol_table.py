class symbol_table:
    def __init__(self):
        self.class_symbol_table = {}
        self.subroutine_symbol_table = {}
        self.running_index_class_field = 0
        self.running_index_class_static = 0
        self.running_index_var = 0
        self.running_index_arg = 0

    
    # Resets the subroutine symbol table
    def clear_subroutine_symbol_table(self):
        self.subroutine_symbol_table.clear()
        self.running_index_var = 0
        self.running_index_arg = 0
    
    # Creates a new identifieir and adds it to corresponding symbol table
    # where name is name of identifier 
    # type is type of identifier 
    # kind is eithier (STATIC, FIELD, ARG, VAR)
    # STATIC, FIELD is class scope 
    # ARG and VAR is subroutine scope
    # (TYPE, KIND, INDEX)
    def define_new_identifier(self, name, type, kind):
        if (kind == "STATIC"):
            self.class_symbol_table[name] = (type, kind, self.running_index_class_static)
            self.running_index_class_static += 1
        elif (kind == "FIELD"):
            self.class_symbol_table[name] = (type, kind, self.running_index_class_field)
            self.running_index_class_field += 1
        elif (kind == "ARG"):
            self.subroutine_symbol_table[name] = (type, kind, self.running_index_arg)
            self.running_index_arg += 1
        elif (kind == "VAR"):
            self.subroutine_symbol_table[name] = (type, kind, self.running_index_var)
            self.running_index_var += 1
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





    

