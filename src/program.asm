    @first_num
    M=0
    @second_num
    M=1
(add_two_previous_store_in_total)
    @total
    M=0
    @first_num
    D=M
    @second_num
    D=D+M
    @total
    M=D
(update_previous_two_values)


    @second_num
    D=M
    @first_num
    M=D
    @total
    D=M
    @second_num
    M=D
// This is extended due to no reason lol 
(a_has_first_and_d_has_second)
    @second_num
    D=M
    @first_num
    A=M
    @add_two_previous_store_in_total
    0;JMP