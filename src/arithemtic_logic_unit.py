from logic_gates import gate
fast_running = True
class alu():
    def __init__(self):
        self.gate = gate()
        pass
    
    # Given two binary bits as strings adds them and returns a string of sum and carry bit
    # return is carry bit followed by sum bit
    # 0, 0 -> 00
    # 0, 1 -> 01
    # 1, 0 -> 01
    # 1, 1 -> 10
    def half_adder(self, a, b):
        carry = self.gate.and_(a, b)
        summ = self.gate.xor(a, b)
        return carry + summ

    # Given 2 binary bits and carry bit as strings adds them and returns a string of sum and carry bit
    # return is carry bit followed by sum bit
    # 0, 0, 0 -> 00
    #
    def full_adder(self, a, b, c):
        carry1, summ = self.half_adder(a, b)
        carry2, summ = self.half_adder(summ, c)

        carry = self.gate.or_(carry1, carry2)
        return carry + summ


    # Given 2 16 bits binary numbers will return the addition of those two numbers
    # Does not handle overflow
    def adder_16_bit(self, a, b):
        carry_bit = 0
        result = ["0" for x in range(16)]
        for x in range(16):
            carry_bit, summ = self.full_adder(b[15 - x], a[15 - x], carry_bit)
            result[15 - x] = summ

        return "".join(result)

    # Given a 16 bit binary number represented as a string will return the increment of that number
    # Does not handle overflow
    def increment_16_bit(self, a):
        one = "0000000000000001"
        return self.adder_16_bit(one, a)

    # Inputs: x[16] y[16]       Two 16-bit data inputs
    #         zx,               Zero the x input
    #         nx,               negate the x input
    #         zy,               zero the y input
    #         ny,               negate the y input
    #         f,                Function code: 1 for Add, 0 for And
    #         no,               negate the output

    # Outputs:  out[16]         16 bit data output
    #           zr,             true iff out = 0
    #           ng,             true iff out < 0

    def alu_16_bit(self, x, y, zx, nx, zy, ny, f, no):
        zeroed_x = self.gate.n_bit_xor(x, x)
        x1 = self.gate.n_bit_multipexor(x, zeroed_x, zx)
        negated_x = self.gate.n_bit_not(x1)
        x2 = self.gate.n_bit_multipexor(x1, negated_x, nx)

        zeroed_y = self.gate.n_bit_xor(y, y)
        y1 = self.gate.n_bit_multipexor(y, zeroed_y, zy)
        negated_y = self.gate.n_bit_not(y1)
        y2 = self.gate.n_bit_multipexor(y1, negated_y, ny)

        added_x_y = self.adder_16_bit(x2, y2)
        and_x_y = self.gate.n_bit_and(x2, y2)

        output  = self.gate.n_bit_multipexor(and_x_y, added_x_y, f)
        negated_output = self.gate.n_bit_not(output)

        out = self.gate.n_bit_multipexor(output, negated_output, no)

        zr = self.gate.n_bit_all_zeros(out)
        ng = out[0]

        return [out, zr, ng]

    # Instead of individual bits put into the ALU we will use defined variables for all the operation
    ZERO = "101010"                     # 0000000000000000
    ONE = "111111"                      # 0000000000000001
    NEGATIVE_ONE = "111010"             # 1111111111111111
    X = "001100"                        # X
    Y = "110000"                        # Y
    BITWISE_NEGATION_X = "001101"       # !X
    BITWISE_NEGATION_Y = "110001"       # !Y
    NEGATIVE_X = "001111"               # -X
    NEGATIVE_Y = "110011"               # -Y
    INCREMENT_X = "011111"              # X+1
    INCREMENT_Y = "110111"              # Y + 1
    DECREMENT_X = "001110"              # X - 1
    DECREMENT_Y = "110010"              # Y - 1
    ADD = "000010"                      # X + Y
    SUB_X_Y = "010011"                  # X - Y
    SUB_Y_X = "000111"                  # Y - X
    BITWISE_AND = "000000"              # X&Y
    BITWISE_OR = "010101"               # X|Y

    # Input:    2 binary numbers (16 bits)
    #           6 digit binary number
    # Output:   binary number (16 bits)

    # Function: Inputs 2 binary number and 6 bit operation into alu
    def alu_n_bit_operation(self, x, y, operation):
        return self.alu_16_bit(x, y, operation[0], operation[1], operation[2], operation[3], operation[4], operation[5])




    """



        N BIT ALU DOWN BELOW



    """

    # Input:            a (n bit), b(n bit)
    # Output:           a+b (n bit) 
    # **Does not handle overflow**
    def adder_n_bit(self, a, b):
        num_bit = len(a)
        carry_bit = 0
        result = ["0" for x in range(num_bit)]

        if (fast_running):
            c = bin(int(a,2) + int(b,2))[2:]
            n = min(num_bit, len(c))
            for x in range(n):
                result[num_bit - x - 1] = c[-1 -x ]
            
            return "".join(result)


            

        for x in range(num_bit):
            carry_bit, summ = self.full_adder(b[num_bit - x - 1], a[num_bit - x - 1], carry_bit)
            result[num_bit - x - 1] = summ

        return "".join(result)
    
    # Input:            a (n bit)
    # Output:           a + 1 (n bit)
    # **Does not handle overflow**
    def increment_n_bit(self, a):
        one = ""
        for x in range(len(a) - 1):
            one += "0"
        one += "1"
        return self.adder_n_bit(one, a)
    
    # Inputs: x[n] y[n]         Two n-bit data inputs 
    # Outputs: [out[n], zr, ng] n bit data output, zero flag, negative flag
    # Function:                 return product of x and y in 2s complement format
    def multiply(self, x, y):
        # Converts a binary number which is in twos complement to integer representation
        def twos_comp(binary_string):
            val, bits = int(binary_string,2), len(binary_string)
            """compute the 2's complement of int value val"""
            if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
                val = val - (1 << bits)        # compute negative value
            return val                         # return positive value as is

        
        def prepend_ones(string, length):
            for x in range(length):
                string = "1" + string
            
            return string

        c = twos_comp(x) * twos_comp(y)


        zr = "0"
        ng = "0"
        if (c == 0):
            zr = "1"
            c = '{0:016b}'.format(c)
        elif (c < 0):
            ng = "1"
            c = bin(c*-1)[2:]
            c = prepend_ones(c, 16-len(c))
        else:
            c = '{0:016b}'.format(c)
        
        
            
            


        
        return [c, zr, ng]

         
        





    # Inputs: x[n] y[n]         Two n-bit data inputs
    #         zx,               Zero the x input
    #         nx,               negate the x input
    #         zy,               zero the y input
    #         ny,               negate the y input
    #         f,                Function code: 1 for Add, 0 for And
    #         no,               negate the output

    # Outputs:  out[n]          n bit data output
    #           zr,             true iff out = 0
    #           ng,             true iff out < 0
    def alu_n_bit(self, x, y, zx, nx, zy, ny, f, no):
        # This multiplication is not good with handling overflow
        if (fast_running and zx == "m"):
            return self.multiply(x, y)


            
            



        zeroed_x = self.gate.n_bit_xor(x, x)
        x1 = self.gate.n_bit_multipexor(x, zeroed_x, zx)
        negated_x = self.gate.n_bit_not(x1)
        x2 = self.gate.n_bit_multipexor(x1, negated_x, nx)

        zeroed_y = self.gate.n_bit_xor(y, y)
        y1 = self.gate.n_bit_multipexor(y, zeroed_y, zy)
        negated_y = self.gate.n_bit_not(y1)
        y2 = self.gate.n_bit_multipexor(y1, negated_y, ny)

        added_x_y = self.adder_n_bit(x2, y2)
        and_x_y = self.gate.n_bit_and(x2, y2)

        output  = self.gate.n_bit_multipexor(and_x_y, added_x_y, f)
        negated_output = self.gate.n_bit_not(output)

        out = self.gate.n_bit_multipexor(output, negated_output, no)

        zr = self.gate.n_bit_all_zeros(out)
        ng = out[0]

        return [out, zr, ng]

    # Input:    x (n-bit), y (n-bit)
    #           operation (6 digit binary number)
    # Output:   binary number (n bits)

    # Function: Inputs 2 binary number and 6 bit operation into alu
    def alu_n_bit_operation(self, x, y, operation):
        
        return self.alu_n_bit(x, y, operation[0], operation[1], operation[2], operation[3], operation[4], operation[5])








