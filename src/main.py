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


jack_Math_class = """
            class Math {
                function int multiply(int x, int y) {
                    var int sum, i, j_bit_y, j; 
                    var int boolean;

                    let i = 1;
                    let j = 0;
                    let sum = 0;

                    while (j < 16) {
                        let j_bit_y = y & i;

                        if (i = j_bit_y) {
                            let sum = sum + x;
                        }

                        let i = i + i;
                        let x = x + x;
                        let j = j + 1;
                                                
                    }

                    return sum;


                }
            }
        """



jack_test_program = """
    
    class Main_Class {
        function void main() {
            do Memory.init();   
            do Screen.setColor(1);
            
            /*do Screen.drawPixel(0, 0);
            do Screen.drawPixel(1, 1);
            do Screen.drawPixel(2, 2);
            do Screen.drawPixel(3, 3);
            do Screen.drawPixel(4, 4);
            do Screen.drawPixel(5, 5);
            do Screen.drawPixel(6, 6);
            do Screen.drawPixel(7, 7);
            do Screen.drawPixel(8, 8);
            do Screen.drawPixel(9, 9);
            do Screen.drawPixel(10, 10);
            do Screen.drawPixel(11, 11);
            do Screen.drawPixel(12, 12);
            do Screen.drawPixel(13, 13);
            do Screen.drawPixel(14, 14);
            do Screen.drawPixel(15, 15);
            do Screen.drawPixel(16, 16);
            do Screen.drawPixel(17, 17);
            do Screen.drawPixel(18, 18);*/

            
            do Screen.drawLine(99, 28, 0, 0);
            /*do Screen.drawLine(0, 15, 15, 0);
            do Screen.drawLine(0, 28, 50, 20);*/

            

            





              
            

            
            
            
            return 0;
        }
    }

"""




def translate_jack_program_to_binary(program):
    lol = comp_engine(program)
    lol.match_jack_program()
    vm = Vm()
    for x in (lol.vm_program.VM_commands_list):
        if (x[:8] == "function"):
            print(x)
        else: 
            print("    " + x)
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
comp.load_program(translate_jack_program_to_binary_with_libraries(jack_test_program + jack_screen_class))
while (True):
    comp.run_N_number_instructions(80000)
    comp.display_screen()
    time.sleep(.15)
    comp.clear_screen()

