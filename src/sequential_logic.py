from arithemtic_logic_unit import alu as a
alu = a()

from logic_gates import gate


"""
    Implements the most primitive sequential element of a computer
    Data Flip Flop
    out(t) = in(t - 1),
    where in and out are the gate’s input and output values and t is the current clock cycle.
"""
class sequential(gate):
    # Assuming always the output bit is always 0
    def __init__(self):
        self.out = 0

    # Data Flip Flop
    # out(t) = in(t - 1),
    # where in and out are the gate’s input and output values and t is the current clock cycle
    def n_bit_dff(self, input):
        self.out = input
        return self.out

    # Input:        In, load (2 Binary bit)
    # Output:       out (Binary bit)
    # Function:     if load(t - 1), then out(t) = in(t - 1)
    #               else out(t) = out(t - 1)
    def bit(self, input, load):
        result = self.multiplexor(self.out, input, load)
        return self.n_bit_dff(result)


    # Input:        In (n bit), load (one bit)
    # Output:       out (n bit )
    # Function:     if load(t - 1), then out(t) = input(t - 1)
    #               else out(t) = out(t - 1)
    # Read:         length n input, load = 0
    # Write:        input, load = 1  
    def register_16_bit(self, input, load):
        result = self.n_bit_multipexor(self.out, input, load)
        return self.n_bit_dff(result) & 0xFFFF

    # Input:        bit, n 
    # Output:       out (n bit)
    # Function:     extended single bit to size n
    def extend_single_bit(self, bit, n):
        extended_bit = ""
        for x in range(n):
            extended_bit += bit

        return extended_bit


    # Input:        in (n bit), inc (bit), load (bit), reset (bit)
    # output:       out (n bit)
    # Function:     if reset(t - 1) then out(t) = 0
    #                   else if load(t-1) then out(t) = in(t - 1)  
    #                       else if inc(t - 1) then out(t) = out(t - 1) + 1
    #                           else out(t) = out(t - 1)     
    def PC_counter_16_bit(self, inp, inc, load, reset):
        extended_out = self.out
        mask = 0xFFFF
        zero = alu.alu_n_bit_operation(inp, inp, alu.ZERO)[0]
        incremented_input = alu.alu_n_bit_operation(extended_out, extended_out, alu.INCREMENT_X)[0] & mask

        # Start from inner most scope of elif and then expand 
        out_inc_elif = self.n_bit_multipexor(extended_out, incremented_input, inc)
        load_elif = self.n_bit_multipexor(out_inc_elif, inp, load)
        reset_elif = self.n_bit_multipexor(load_elif, zero, reset)

        result = self.register_16_bit(reset_elif, 1)
        return result
