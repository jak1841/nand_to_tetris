from arithemtic_logic_unit import alu

# j = alu()
# a = "0000000000000000"
# b = "0000000000000001"
# print(j.adder_16_bit(a, b))

from sequential_logic import seq
s = seq("0")

print(s.SR_AND_OR_latch("1", "0"))
print(s.SR_AND_OR_latch("0", "1"))

