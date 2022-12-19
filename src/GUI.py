import os 
from random_access_memory import Ram_n
os.system("clear")

# Screen size: 128 x 176

screen = Ram_n(2048, 16)

from arithemtic_logic_unit import alu as a

# Given an array of 32 16 bit data will display one row of the computer where each 1 bit will be 
def print_row_to_screew(array):
    row = ""
    for x in array:
        for y in x:
            if (y == "1"):
                row+= "■"
            else:
                row += " "
        
    
    print(row)

def update_screen():
    print("updating screen")
    

def change_pixel_at():
    global screen
    alu = a()
    position = "0000000000000000"


    for x in range(128):
        for y in range(11):
            screen.do_operation("1111111111111111", position, "1")
            position = alu.increment_n_bit(position)



    

        

change_pixel_at()