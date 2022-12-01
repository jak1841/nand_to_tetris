
from logic_gates import sequential as seq
from logic_gates import gate as g

gate = g()


# Given an n, n = s^x for some n implements the RAM part of the computer
# Where n is the number of registers in the operation
class Ram_n:
    def __init__(self, N):
        init_registers_array(N, 16)

    # Makes N registers with width:= width and puts it into registers_array 
    # All registers will be be initialized to 0. 
    def init_registers_array(self, N, width):
        zero = ""
        for y in range(width):
            zero+="0"

        self.registers_array = []
        for x in range(n):
            new_register = seq()
            new_register.register_n_bit(zero, 1)
            self.registers_array.append(new_register)
    
    # Input:        in (n bit), address (k bit)[2^k = N], load (bit)
    # Output:       out
    # Function:     output(t) = Ram[address(t)](t)
    #               if load(t - 1) then 
    #                   Ram[address(t - 1)](t) = in (t - 1)
    
        
        
