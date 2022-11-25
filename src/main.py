from arithemtic_logic_unit import alu

# j = alu()
# a = "0000000000000000"
# b = "0000000000000001"
# print(j.adder_16_bit(a, b))

from sequential_logic import seq
s = seq("0")
print(s.d_latch("0", "0"))

s = seq("1")
print(s.d_latch("0", "0"))




