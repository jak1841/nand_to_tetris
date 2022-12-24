from random_access_memory import Ram_n

# Screen size: 112 x 176

screen = Ram_n(1280, 16)

from arithemtic_logic_unit import alu as a

# Given an array of 32 16 bit data will display one row of the computer where each 1 bit will be 
def convert_binary_to_screen(string):
    row = ""
    for x in string:
        if (x == "1"):
            row+= "■"
        else:
            row += " "
    return row

def update_screen():
    print("updating screen")
    string_screen = ""
    memory = screen.get_list_of_all_register_values()
    

    for x in range(128):
        temp = ""
        for y in range(10):
            temp+= memory[10*x + y]
        string_screen += convert_binary_to_screen(temp) + "\n"
    
    print(string_screen)

def convert_decimal_to_binary(decimal):
    return str(bin(decimal))[2:]

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def change_pixel_at():
    global screen
    alu = a()
    position = "0000000000000000"


    for x in range(1280):
        screen.do_operation("1111111111111111", position, "1")
        position = alu.increment_n_bit(position)
    
    screen.do_operation("0000000000000001",  convert_decimal_to_binary(1279),  "1")





        

change_pixel_at()

update_screen()