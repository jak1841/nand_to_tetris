from Jack_compilation_engine import comp_engine 
from Virtual_machine import Vm
from hack_assembler import assembler
from hack_computer import computer
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
    class Point {
    
        field int x, y;
        constructor Point new(int x1, int y1) {
            /* Source of error is in the field let statement*/
            let x = x1;
            let y = y1;
            return this;
        }

        function int get_x() {
            return x;
        }

        function int get_y() {
            return y;
        }


    }
    class Main_Class {
        static int g;

        function int multi(int x, int y) {
            var int j, i, sum;
            let sum = 0;
            let j = 0;
            let i = 1;


            while (j < 15) {
                
                if (j < 15) {
                    let sum = sum + 1;
                } 
                let j = j + 1;
                
            }

            return sum;
        }

        function void main() {
            var Memory john;
            var int k;
            var Point p, d;

            let p = 1;
            let d = 2;

            

            do Memory.init();        
            
            do Memory.poke(801, Main_Class.multi(2, 3));


            
    

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

     
     




comp = computer()
comp.load_program(translate_jack_program_to_binary(jack_memory_class_first_fit + jack_test_program))
comp.run_N_number_instructions(40000)

print(comp.data_memory.memory[800:803])

print(comp.data_memory.memory[2048:2050])
