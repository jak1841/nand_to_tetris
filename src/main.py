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

jack_test_program = """
    class bruh {
        static int l, bruh;
        method void deeznuts () {
            var int i;
            let i = 0;
            let l = 0;

            while (i < 20) {
                let l = l + 5;
                let i = i + 1;
            }
            
        }
    }

"""

def translate_jack_program_to_binary(program):
    lol = comp_engine(program)
    lol.match_class()
    vm = Vm()
    print(lol.vm_program.VM_commands_list)
    assembly_instructions= vm.get_hack_assembly_instructions_from_VM_instructions(lol.vm_program.VM_commands_list)
    ass = assembler()
    return ass.array_hack_assembly_instruction_to_binary_instruction(assembly_instructions)

     
     




comp = computer()
comp.load_program(translate_jack_program_to_binary(jack_test_program))
comp.run_N_number_instructions(21000)

print(comp.data_memory.memory[16])