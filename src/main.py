from Jack_compilation_engine import comp_engine 
from Virtual_machine import Vm
from hack_assembler import assembler
from hack_computer import computer
import time
jack_program = """

class Iloveyoumomma {
    static nool james, bruh, jame;
    
    field int cuh, size;

    method void incSize() {
        var int sum, index;
        var int index ;
        
    }

    

    function boolean momme_get_better(int Iloveyou, boolean is_safe, int koko) {
        var Array please_waheguru;
        var boolean Iwill_pray;
    }

    method void incSize(int x) {
                if (x) {
                    do erase();
                    let size=size;
                    do draw();
                }
                return;
            }
    
    method void incSize(int x, int y) {
                if (((y + size) < 254) &
                    ((x + size) < 510)) {
                    do erase();
                    let size = size + 2;
                    do draw();
                }
                return;
            }
    
    method int average(Array numbers, int array_length) {
                var int sum;
                var int index;
                let index = 0;
                let sum = 0;

                while (index < array_length) {
                    let sum = sum + numbers[index];
                    let index = index+1;
                }

                return (sum/array_length);
            }
    
}

"""

jack_memory_class = """
    class Memory {
        static int ram; 
        static int heap_base;

        /* Called in sys.init function always*/
        function void init() {
            let heap_base = 2048;
            let ram = 0;
            return 0;
        }

        /*  Get value at that address in RAM */
        function int peek(int address) {
            return ram[address];
        }

        /* Update value at given address with given value in RAM */
        function void poke(int address, int value) {
            let ram[address] = value;
            return 0;
        }

        /* Allocates n different memory position */
        function int alloc(int n) {
            var int block; 
            let block = heap_base;
            let heap_base = heap_base + n;

            return block;
        }

        /* Deallocates a object given its pointer*/
        function void deAlloc (int object_address) {
            return 0;
        }
    }

"""

jack_memory_class_first_fit = """
    class Memory {
        static int ram; 
        static Array heap;
        static int freeList;

        /* Called in sys.init function always*/
        function void init() {
            let heap = 2048;
            let ram = 0;
            let freeList = heap;
            let freeList[0] = 0;
            let freeList[1] = 14334;
            return 0;
        }

        /*  Get value at that address in RAM */
        function int peek(int address) {
            return ram[address];
        }

        /* Update value at given address with given value in RAM */
        function void poke(int address, int value) {
            let ram[address] = value;
            return 0;
        }

        /* Allocates n different memory position */
        function int alloc(int n) {
            /*
                Iterates through the free list and checks if a block is available
            */
            var int cur, i;
            var int block;
            let cur = freeList; 

            let i = 0;

            /* Cur gets to eithier last position and does not have an */
            while (cur > 0) {

                
                if (cur[1] > (n + 2)) {
                    let block = cur + cur[1] - (n + 2);
                    let block[0] = 0;
                    let block[1] = n;
                    let cur[1] = cur[1] - (n + 2);
                    return block + 2;
                }

                let cur = cur[0];

            }

            return 2048; /*Failure to find block*/ 
        }

        /* Deallocates a object given its pointer*/
        function void deAlloc (int object_address) {
            var int pointer_object, cur;
            let cur = freeList;

            while (cur[0] > 0) {
                let cur = cur[0];
            } 

            let pointer_object = object_address - 2;
            let cur[0] = pointer_object;

            return -1; /* Success */
        }
    }

"""




jack_test_program = """
    
    class Main_Class {
        function void main() {
            var Array a;
            do Memory.init();   
            do Output.init();
            do Screen.setColor(1);

            





            
            do Output.printChar(0, 0, 0);
            do Output.printChar(1, 4, 0);
            do Output.printChar(2, 8, 0);
            do Output.printChar(3, 12, 0);
            do Output.printChar(4, 16, 0);
            do Output.printChar(5, 20, 0);
            do Output.printChar(6, 24, 0);
            do Output.printChar(7, 28, 0);
            do Output.printChar(8, 32, 0);
            do Output.printChar(9, 36, 0);
            do Output.printChar(10, 40, 0);
            do Output.printChar(11, 44, 0);
            do Output.printChar(12, 48, 0);
            do Output.printChar(13, 52, 0);
            do Output.printChar(14, 56, 0);
            do Output.printChar(15, 60, 0);
            do Output.printChar(16, 64, 0);
            do Output.printChar(17, 68, 0);

            do Output.printChar(18, 72, 0);
            do Output.printChar(19, 76, 0);
            do Output.printChar(20, 80, 0);
            do Output.printChar(21, 84, 0);
            do Output.printChar(22, 88, 0);
            do Output.printChar(23, 92, 0);
            do Output.printChar(24, 96, 0);
            do Output.printChar(25, 0, 4);
            do Output.printChar(26, 4, 4);

            do Output.printChar(27, 8, 4);
            do Output.printChar(28, 12, 4);
            do Output.printChar(29, 16, 4);
            do Output.printChar(30, 20, 4);
            do Output.printChar(31, 24, 4);
            do Output.printChar(32, 28, 4);
            do Output.printChar(33, 32, 4);
            do Output.printChar(34, 36, 4);
            do Output.printChar(35, 40, 4);


            



            
            return 0;
        }
    }

"""

jack_output_class = """
    class Output {
        /*A ascii value will start at 0 and go on until we reach the */
        static Array charMaps; 
        /*This class is where we actually implement the text output and is based off the screen class
        
            All Characters are created in 3x3 grid and one space horizontal and vertical to seperate other characters 

            Characters will be uppercase letters, numbers, and spaces
        */
        function void init() {
            do Screen.init();
            let charMaps = Array.new(36);
            do Output.add_character_bit_map(0, 0, 1, 0, 1, 1, 1, 1, 0, 1); /*A*/
            do Output.add_character_bit_map(1, 1, 1, 0, 1, 1, 1, 1, 1, 1); /*B*/
            do Output.add_character_bit_map(2, 1, 1, 1, 1, 0, 0, 1, 1, 1); /*C*/
            do Output.add_character_bit_map(3, 1, 1, 0, 1, 0, 1, 1, 1, 0); /*D*/
            do Output.add_character_bit_map(4, 1, 1, 1, 1, 1, 0, 1, 1, 1); /*E*/
            do Output.add_character_bit_map(5, 1, 1, 1, 1, 1, 0, 1, 0, 0); /*F*/
            do Output.add_character_bit_map(6, 1, 1, 0, 1, 0, 1, 1, 1, 1); /*G*/
            do Output.add_character_bit_map(7, 1, 0, 1, 1, 1, 1, 1, 0, 1); /*H*/
            do Output.add_character_bit_map(8, 1, 1, 1, 0, 1, 0, 1, 1, 1); /*I*/
            do Output.add_character_bit_map(9, 0, 0, 1, 1, 0, 1, 1, 1, 1); /*J*/
            do Output.add_character_bit_map(10, 1, 0, 1, 1, 1, 0, 1, 0, 1); /*K*/
            do Output.add_character_bit_map(11, 1, 0, 0, 1, 0, 0, 1, 1, 1); /*L*/
            do Output.add_character_bit_map(12, 1, 1, 1, 1, 1, 1, 1, 0, 1); /*M*/
            do Output.add_character_bit_map(13, 1, 1, 1, 1, 0, 1, 1, 0, 1); /*N*/
            do Output.add_character_bit_map(14, 1, 1, 1, 1, 0, 1, 1, 1, 1); /*O*/
            do Output.add_character_bit_map(15, 1, 1, 1, 1, 1, 1, 1, 0, 0); /*P*/
            do Output.add_character_bit_map(16, 1, 1, 1, 1, 1, 1, 0, 0, 1); /*Q*/
            do Output.add_character_bit_map(17, 1, 1, 1, 1, 0, 0, 1, 0, 0); /*R*/
            do Output.add_character_bit_map(18, 0, 1, 1, 0, 1, 0, 1, 1, 0); /*S*/
            do Output.add_character_bit_map(19, 1, 1, 1, 0, 1, 0, 0, 1, 0); /*T*/
            do Output.add_character_bit_map(20, 1, 0, 1, 1, 0, 1, 1, 1, 1); /*U*/
            do Output.add_character_bit_map(21, 1, 0, 1, 1, 0, 1, 0, 1, 0); /*V*/
            do Output.add_character_bit_map(22, 1, 0, 1, 1, 1, 1, 1, 1, 1); /*W*/
            do Output.add_character_bit_map(23, 1, 0, 1, 0, 1, 0, 1, 0, 1); /*X*/
            do Output.add_character_bit_map(24, 1, 0, 1, 0, 1, 0, 0, 1, 0); /*Y*/
            do Output.add_character_bit_map(25, 1, 1, 0, 0, 1, 0, 0, 1, 1); /*Z*/

            do Output.add_character_bit_map(26, 1, 1, 1, 1, 0, 1, 1, 1, 1); /*0*/
            do Output.add_character_bit_map(27, 1, 1, 0, 0, 1, 0, 1, 1, 1); /*1*/
            do Output.add_character_bit_map(28, 1, 1, 0, 0, 1, 0, 0, 1, 1); /*2*/
            do Output.add_character_bit_map(29, 1, 1, 1, 0, 1, 1, 1, 1, 1); /*3*/
            do Output.add_character_bit_map(30, 1, 0, 1, 1, 1, 1, 0, 0, 1); /*4*/
            do Output.add_character_bit_map(31, 0, 1, 1, 0, 1, 0, 1, 1, 0); /*5*/
            do Output.add_character_bit_map(32, 1, 0, 0, 1, 1, 1, 1, 1, 1); /*6*/
            do Output.add_character_bit_map(33, 1, 1, 1, 0, 0, 1, 0, 0, 1); /*7*/
            do Output.add_character_bit_map(34, 0, 1, 1, 1, 1, 1, 1, 1, 1); /*8*/
            do Output.add_character_bit_map(35, 1, 1, 1, 1, 1, 1, 0, 0, 1); /*9*/







            



            return null;
        }

        /*Add a character at ascii_value acooitated into charMaps. a-i is going to be eithier 0 or 1*/
        function void add_character_bit_map(int ascii_value, int a, int b, int c, int d, int e, int f, int g, int h, int i) {
            var Array temp;
            let temp = Array.new(9);
            let temp[0] = a;
            let temp[1] = b;
            let temp[2] = c;
            let temp[3] = d;
            let temp[4] = e;
            let temp[5] = f;
            let temp[6] = g;
            let temp[7] = h;
            let temp[8] = i;

            let charMaps[ascii_value] = temp;
            return null;
        }

        function void printChar(int ascii_value, int x, int y) {
            var Array temp;
            let temp = charMaps[ascii_value];
            if (temp[0] = 1) {
                do Screen.drawPixel(x, y);
            }
            if (temp[1] = 1) {
                do Screen.drawPixel(x + 1, y);
            }
            if (temp[2] = 1) {
                do Screen.drawPixel(x + 2, y);
            }
            if (temp[3] = 1) {
                do Screen.drawPixel(x, y + 1);
            }
            if (temp[4] = 1) {
                do Screen.drawPixel(x + 1, y + 1);
            }
            if (temp[5] = 1) {
                do Screen.drawPixel(x + 2, y + 1);
            }
            if (temp[6] = 1) {
                do Screen.drawPixel(x, y + 2);
            }
            if (temp[7] = 1) {
                do Screen.drawPixel(x + 1, y + 2);
            }
            if (temp[8] = 1) {
                do Screen.drawPixel(x + 2, y + 2);
            }

            return null;

            
        }




    }

"""



def translate_jack_program_to_binary(program):
    lol = comp_engine(program)
    lol.match_jack_program()
    vm = Vm()
    assembly_instructions= vm.get_hack_assembly_instructions_from_VM_instructions(lol.vm_program.VM_commands_list)
    ass = assembler()
    return ass.array_hack_assembly_instruction_to_binary_instruction(assembly_instructions)

     
def translate_jack_program_to_binary_with_libraries(program):
    lol = comp_engine(program)
    lol.add_all_libraries_to_tokens()
    lol.match_jack_program()
    vm = Vm()
    assembly_instructions= vm.get_hack_assembly_instructions_from_VM_instructions(lol.vm_program.VM_commands_list)
    ass = assembler()
    return ass.array_hack_assembly_instruction_to_binary_instruction(assembly_instructions)



import sys
import os
comp = computer()
print(len(translate_jack_program_to_binary_with_libraries(jack_test_program)))
comp.load_program(translate_jack_program_to_binary_with_libraries(jack_test_program + jack_output_class))

while (True):
    comp.run_N_number_instructions(80000)
    comp.display_screen()
    time.sleep(.25)
    comp.clear_screen()

