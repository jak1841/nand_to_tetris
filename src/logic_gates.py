"""

    Implementing low level logic gates

"""
class gate:
    def __init__(self):
        pass

    # 0, 0 -> 1
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 0
    # Given 2 single bit both in the form of string, returns a bit speceficed by nand operation
    def nand(self, a, b):
        return ~(a & b)

    # 0 -> 1
    # 1 -> 0
    # Given a single bit in the form of string, returns a bit specefied by not operation
    def not_(self, a):
        return self.nand(a, a) 

    # 0, 0 -> 0
    # 0, 1, -> 0
    # 1, 0 -> 0
    # 1, 1 -> 1
    # Given 2 single bit both in the form of string, returns a bit specefied by and operation
    def and_(self, a, b):
        return self.not_(self.nand(a, b))

    # 0, 0 -> 0
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 1
    # Given 2 single bit both as string return a bit of the or operation
    def or_(self, a, b):
        return self.nand(self.not_(a), self.not_(b))

    # 0, 0 -> 0
    # 0, 1, -> 1
    # 1, 0 -> 1
    # 1, 1 -> 0
    # Given 2 single bit both as string return a bit of the xor operation
    def xor(self, a, b):
        not_ab = self.and_(self.not_(a), b)
        b_nota = self.and_(self.not_(b), a)
        return self.or_(not_ab, b_nota)

    # a!sel or bsel -> 1
    # Given 2 single bit and a selector bit will return a bit of the multiplexor operation
    # sel = 0 -> output equal a
    # sel = 1 -> output equal b
    def multiplexor(self, a, b, sel):
        a_not_sel = self.and_(a, self.not_(sel))
        b_sel = self.and_(b, sel)
        return self.or_(a_not_sel, b_sel)

    # given a single input bit and a selector bit will return two bits of the form of string doing demultiplexor operation
    # in!sel -> a
    # insel -> b
    def demultiplexor(self, input, sel):
        a = self.and_(input, self.not_(sel))
        b = self.and_(input, sel)
        return [a, b]

    # Input:    2 Binary number(both length N), selector bit
    # Ouput:    Binary number
    # Mulitplexor but with n bit data.
    def n_bit_multipexor (self, a, b, sel):
        if (sel == 0):
            return a
        return b

    # Input:    Binary number (length N), selector bit
    # Ouput:    List of two binary numbers (Length N), Where first Index = a, 2nd index = b.
    # Demultiplexor with n bit input
    def n_bit_demultplexor(self, input, sel):
        result = [0, 0]
        if (sel == 0):
            result[0] = input
        else:
            result[1] = input
        return result
    # Input:    2 binary numbers (Length N)
    # output:   binary number (Length N)
    # xor of both binary number
    def n_bit_xor(self, a, b):
        return self.xor(a, b)

    # Input:    2 binary numbers (Length N)
    # Ouput:    binary number (Length N)
    # OR of two binary numbers
    def n_bit_or(self, a, b):
        return self.or_(a, b)        

    # Input:    2 binary numbers (Length N)
    # Output:   binary number (Length N)
    # And of two binary numbers
    def n_bit_and(self, a, b):
        return self.and_(a, b)
        

    # Input:    Binary number (Length N)
    # Output:   Binary number (Length N)
    # NOT of binary number
    def n_bit_not(self, a):
       return self.not_(a) 

    # Input:    2 Binary number (Length N)
    # Output:   Binary number (Length N)
    # NAND of binary numbers
    def n_bit_nand(self, a, b):
        return self.nand(a, b)

    # Input: Binary number (Length N)
    # Output Single bit
    # if all bits are 0 -> 1
    # else -> 0
    def n_bit_all_zeros(self, a):
        result = a == 0
        if (result):
            return 0x1
        return 0x0


    # Input:    4 Binary number(all length N), selector binary number (length 2)
    # Ouput:    Binary number (Length N)
    # 4 way Mulitplexor but with n bit data.
    # sel = 00 -> a
    # sel = 01 -> b
    # sel = 10 -> c
    # sel = 11 -> d
    def n_bit_4_way_multiplexor(self, a, b, c, d, sel):
        result_1 = self.n_bit_multipexor(a, b, sel & 0x1)
        result_2 = self.n_bit_multipexor(c, d, sel & 0x1)
        return self.n_bit_multipexor(result_1, result_2, (sel & 0x2) >> 1)

    # Input:    array of length n, such that n = 2^x for some x (all length N), selector binary (length x)
    # output:   Binary number (length n)
    # n way multiplexor but with n bit data
    def n_bit_n_way_multiplexor(self, list_n_binary_nums, sel):
        if (sel <= 0x1):
            return self.n_bit_multipexor(list_n_binary_nums[0], list_n_binary_nums[1], sel)

        numBitsSel = sel.bit_length() - 1
        mask = (0x1 << (numBitsSel - 1)) 
        midpoint = int(len(list_n_binary_nums)/2)
        r1 = self.n_bit_n_way_multiplexor(list_n_binary_nums[0:midpoint], sel & mask >> 1)
        r2 = self.n_bit_n_way_multiplexor(list_n_binary_nums[midpoint:], sel & mask)
        return self.n_bit_multipexor(r1, r2, sel & 0x1)


    # Input:        input (n bit), address
    # output:       output_array (2^len(address) in length)     
    # n way demultiplexor with n bit data 
    def n_bit_n_way_demultiplexor(self, input, address):
        if (len(address) == 1):
            return self.n_bit_demultplexor(input, address[0])

        result = self.n_bit_demultplexor(input, address[0])
        return self.n_bit_n_way_demultiplexor(result[0], address[1:]) + self.n_bit_n_way_demultiplexor(result[1], address[1:])
        
    # Input:        list_n_binary numbers (each 1 bit)
    # output:       1 bit
    # Function:     n multiway or 