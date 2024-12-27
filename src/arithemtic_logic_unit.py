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
        return (carry, summ)

    # Given 2 binary bits and carry bit as strings adds them and returns a string of sum and carry bit
    # return is carry bit followed by sum bit
    # 0, 0, 0 -> 00
    #
    def full_adder(self, a, b, c):
        carry1, summ = self.half_adder(a, b)
        carry2, summ = self.half_adder(summ, c)

        carry = self.gate.or_(carry1, carry2)
        return (carry, summ)


    # Given 2 16 bits binary numbers will return the addition of those two numbers
    # Does not handle overflow
    def adder_16_bit(self, a, b):
        return (a + b) & 0xFFFF 

    # Given a 16 bit binary number represented as a string will return the increment of that number
    # Does not handle overflow
    def increment_16_bit(self, a):
        one = 0x0001
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
        mask = 0xFFFF
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

        output  = self.gate.n_bit_multipexor(and_x_y, added_x_y, f) & mask
        negated_output = self.gate.n_bit_not(output) & mask

        out = self.gate.n_bit_multipexor(output, negated_output, no)

        zr = self.gate.n_bit_all_zeros(out)
        ng = out >> 15

        return [out, zr, ng]

    # Instead of individual bits put into the ALU we will use defined variables for all the operation
    ZERO = 0b101010                     # 0000000000000000
    ONE = 0b111111                      # 0000000000000001
    NEGATIVE_ONE = 0b111010             # 1111111111111111
    X = 0b001100                        # X
    Y = 0b110000                        # Y
    BITWISE_NEGATION_X = 0b001101       # !X
    BITWISE_NEGATION_Y = 0b110001       # !Y
    NEGATIVE_X = 0b001111               # -X
    NEGATIVE_Y = 0b110011               # -Y
    INCREMENT_X = 0b011111              # X+1
    INCREMENT_Y = 0b110111              # Y + 1
    DECREMENT_X = 0b001110              # X - 1
    DECREMENT_Y = 0b110010              # Y - 1
    ADD = 0b000010                      # X + Y
    SUB_X_Y = 0b010011                  # X - Y
    SUB_Y_X = 0b000111                  # Y - X
    BITWISE_AND = 0b000000              # X&Y
    BITWISE_OR = 0b010101               # X|Y
    MULTIPLY = 0b100001                 # X*Y
    DIVIDE = 0b000001                   # X/Y

    # Input:    2 binary numbers (16 bits)
    #           6 digit binary number
    # Output:   binary number (16 bits)

    # Function: Inputs 2 binary number and 6 bit operation into alu
    def alu_n_bit_operation(self, x, y, operation):
        if (operation == alu.MULTIPLY):
            return self.multiply(x, y)
        if (operation == alu.DIVIDE and y != 0):
            return self.divide(x, y)

        return self.alu_16_bit(x, y, operation & 0x20, operation & 0x10, operation & 0x8, operation & 0x4, operation & 0x2, operation & 0x1)




    """



        N BIT ALU DOWN BELOW



    """

    # Input:            a (n bit), b(n bit)
    # Output:           a+b (n bit) 
    # **Does not handle overflow**
    def adder_n_bit(self, a, b):
        numDigits = max(a.bit_length(), b.bit_length()) 
        mask = (0x1 << numDigits) - 1
        return (a + b) & mask

    # Input:            a (n bit)
    # Output:           a + 1 (n bit)
    # **Does not handle overflow**
    def increment_n_bit(self, a):
        return self.adder_n_bit(0x1, a)
    
    # Inputs: x[n] y[n]         Two n-bit data inputs 
    # Outputs: [out[n], zr, ng] n bit data output, zero flag, negative flag
    # Function:                 return product of x and y in 2s complement format
    def multiply(self, x, y):
        x = x & 0xFFFF
        y = y & 0xFFFF

        if (x & 0x8000):
            x-=0x10000
        if (y & 0x8000):
            y-=0x10000

        c = int(x * y) 

        zr = 0
        ng = 0
        if (c == 0):
            zr = 1
        elif (c < 0):
            c -= 0x10000
            ng = 1
        
        c = c & 0xFFFF
        return [c, zr, ng]

         
    # Inputs x[n], y[n]         Two n-bit data inputs 
    # Outputs: [out[n], zr, ng] n bit data output, zero flag, negative flag 
    # Function:                 return division of x/y in 2s complement format
    def divide(self, x, y):
        x = x & 0xFFFF
        y = y & 0xFFFF

        if (x & 0x8000):
            x-=0x10000
        if (y & 0x8000):
            y-=0x10000

        c = int(x / y) 

        zr = 0
        ng = 0
        if (c == 0):
            zr = 1
        elif (c < 0):
            c -= 0x10000
            ng = 1
        
        c = c & 0xFFFF
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
        
        # This division is not good with handling overflow
        if (fast_running and zx == "d"):
            return self.divide(x, y)


            
            



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
