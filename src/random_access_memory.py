
from sequential_logic import sequential as seq
from logic_gates import gate as g

gate = g()


# Given an n, n = 2^x for some n implements the RAM part of the computer
# Where n is the number of registers in the operation
class Ram_n:
    def __init__(self, N, width):
        self.width = width
        self.init_memory(N, self.width)

    # Makes N registers with width:= width and puts it into registers_array 
    # All registers will be be initialized to 0. 
    def init_memory(self, N, width):
        self.memory = []
        for x in range(N):
            self.memory.append(0)
    
    # Input:        in (n bit), address (k bit)[2^k = N], load (bit)
    # Output:       out
    # Function:     output(t) = Ram[address(t)](t)
    #               if load(t - 1) then 
    #                   Ram[address(t - 1)](t) = in (t - 1)
    def do_operation(self, input, address, load):
        
        try: 
            if (load == 1):
                self.memory[address] = input
                return self.memory[address]
            else:
                return self.memory[address]
        except:
            raise Exception("Index out of Bounds for RAM")


        
        
    def get_list_of_all_register_values(self):
        return self.memory
            



        

            



        
        
