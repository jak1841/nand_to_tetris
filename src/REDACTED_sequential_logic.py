
"""
    The purpose of this class is to implement sequential logic that is have the
    ability to to store bits and preserve values over time.

"""

from logic_gates import gate
class seq(gate):
    def __init__(self, prev_output):
        self.previous_output = prev_output


    # Input:        Two binary bit
    # Output:       Binary bit
    # Function:     S: 0, R:0 -> no change, random initial
    #               S: 1, R:0 -> Q = 1
    #               S: X, R:1 -> Q = 0
    def SR_AND_OR_latch(self, s, r):
        not_r = self.not_(r)
        or_result = self.or_(s, self.previous_output)
        self.previous_output = self.and_(not_r, or_result)
        return self.previous_output

    # Input:        2 Binary bit
    # Output:       Binary bit
    # Function:     D: 0 enable: 0 -> no change
    #               D: 1 enable: 0 -> no change
    #               D: 0 enable: 1 -> Q = 0
    #               D: 1 enable: 1 -> Q = 1
    def d_latch(self, d, enable):
        d_not = self.not_(d)
        not_and = self.and_(d_not, enable)
        and_ = self.and_(d, enable)
        return self.SR_AND_OR_latch(and_, not_and)




