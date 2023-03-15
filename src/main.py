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
            do Screen.setColor(1);

            let a = Array.new(20);
            let a[0] = 1;
            let a[10] = 21;

            let a[19] = 63;

            do Memory.poke(800, a);





                    
            /*do Output.printChar(65, 0, 0);
            do Output.printChar(66, 4, 0);
            do Output.printChar(67, 8, 0);
            do Output.printChar(68, 12, 0);
            do Output.printChar(69, 16, 0);
            do Output.printChar(70, 20, 0);
            do Output.printChar(71, 24, 0);
            do Output.printChar(72, 28, 0);
            do Output.printChar(73, 32, 0); 
            do Output.printChar(74, 36, 0); 
            do Output.printChar(75, 40, 0);
            do Output.printChar(76, 44, 0);
            do Output.printChar(77, 48, 0);  
            do Output.printChar(78, 52, 0);
            do Output.printChar(79, 56, 0);
            do Output.printChar(80, 60, 0);
            do Output.printChar(81, 64, 0);
            do Output.printChar(82, 68, 0);
            do Output.printChar(83, 72, 0);
            do Output.printChar(84, 76, 0);
            do Output.printChar(85, 80, 0);
            do Output.printChar(86, 84, 0);
            do Output.printChar(87, 88, 0);
            do Output.printChar(88, 92, 0);
            do Output.printChar(89, 96, 0);
            do Output.printChar(90, 0, 4);*/

            



            
            return 0;
        }
    }

"""

jack_output_class = """
    class Output {
        /*This class is where we actually implement the text output and is based off the screen class
        
            All Characters are created in 3x3 grid and one space horizontal and vertical to seperate other characters 

            Characters will be uppercase letters, numbers, and spaces
        */
        function void init() {
            do Screen.init();
            return null;
        }

        /* Given a character ascii will print that character at some position on the screen */
        function void printChar(int ascii_value, int x, int y) {
            /*A*/
            if (ascii_value = 65) {
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*B*/
            if (ascii_value = 66) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*C*/
            if (ascii_value = 67) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            } 

            /*D*/
            if (ascii_value = 68) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
            }

            /*E*/
            if (ascii_value = 69) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);

            }

            /*F*/
            if (ascii_value = 70) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
            }

            /*G*/
            if (ascii_value = 71) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*H*/
            if (ascii_value = 72) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*I*/
            if (ascii_value = 73) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*J*/
            if (ascii_value = 74) {
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*K*/
            if (ascii_value = 75) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*L*/
            if (ascii_value = 76) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x, y+1);
                do Screen.drawPixel(x, y+2);
                do Screen.drawPixel(x + 1, y+2);
                do Screen.drawPixel(x + 2, y+2);
            }

            /*M*/
            if (ascii_value = 77) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*N*/
            if (ascii_value = 78) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*O*/
            if (ascii_value = 79) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*P*/
            if (ascii_value = 80) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
            }

            /*Q*/
            if (ascii_value = 81) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*R*/
            if (ascii_value = 82) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x, y + 2);
            }

            /*S*/
            if (ascii_value = 83) {
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
            }
            /*T*/
            if (ascii_value = 84) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 1, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 1, y + 2);
            }

            /*U*/
            if (ascii_value = 85) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }
            /*V*/
            if (ascii_value = 86) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x + 1, y + 2);
            }

            /*W*/
            if (ascii_value = 87) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x, y + 1);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 2, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 1, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }
            /*X*/
            if (ascii_value = 88) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x, y + 2);
                do Screen.drawPixel(x + 2, y + 2);
            }

            /*Y*/
            if (ascii_value = 89) {
                do Screen.drawPixel(x, y);
                do Screen.drawPixel(x + 2, y);
                do Screen.drawPixel(x + 1, y + 1);
                do Screen.drawPixel(x + 1, y + 2);
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
comp.load_program(translate_jack_program_to_binary_with_libraries(jack_test_program ))
comp.run_N_number_instructions(40000)

print(comp.data_memory.memory[800])
print(comp.data_memory.memory[16362: 16382])

# while (True):
#     comp.run_N_number_instructions(80000)
#     comp.display_screen()
#     time.sleep(.25)
#     comp.clear_screen()

