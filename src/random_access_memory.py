
from sequential_logic import sequential as seq
from logic_gates import gate as g

gate = g()


# Given an n, n = 2^x for some n implements the RAM part of the computer
# Where n is the number of registers in the operation
class Ram_n:
    def __init__(self, N, width):
        self.width = width
        self.init_registers_array(N, self.width)

    # Makes N registers with width:= width and puts it into registers_array 
    # All registers will be be initialized to 0. 
    def init_registers_array(self, N, width):
        zero = ""
        for y in range(width):
            zero+="0"

        self.registers_array = []
        for x in range(N):
            new_register = seq()
            new_register.register_n_bit(zero, 1)
            self.registers_array.append(new_register)
    
    # Input:        in (n bit), address (k bit)[2^k = N], load (bit)
    # Output:       out
    # Function:     output(t) = Ram[address(t)](t)
    #               if load(t - 1) then 
    #                   Ram[address(t - 1)](t) = in (t - 1)
    def do_operation(self, input, address, load):
        # Goes through and produces 2^(len(address)) inputs with load bit prepended
        # To be used for all list_registers as input with load bit
        new_input = load + input
        list_inputs = gate.n_bit_n_way_demultiplexor(new_input, address)

        list_register_values = []   # Stores the output of every register value after updating it 
        
        # Updates each register with load bit and input from previous code
        for x in range(len(self.registers_array)):
            inp = list_inputs[x][1:]
            load_bit = list_inputs[x][0]
            list_register_values.append(self.registers_array[x].register_n_bit(inp, load_bit))
        
        # Takes register values and returns one based off of its address 
        return gate.n_bit_n_way_multiplexor(list_register_values, address)
        
        
    def get_list_of_all_register_values(self):
        zero = ""
        for x in range(self.width):
            zero += "0"

        temp = []
        for x in range(len(self.registers_array)):
            temp.append(self.registers_array[x].register_n_bit(zero, 0))
        
        return temp
            



        

            



        
        
