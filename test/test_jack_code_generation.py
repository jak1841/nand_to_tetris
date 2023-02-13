import unittest
import sys
# allows use of moducles
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/nand_to_tetris/src')

from Jack_compilation_engine import comp_engine 
from Virtual_machine import Vm
from hack_assembler import assembler
from hack_computer import computer



class Test(unittest.TestCase):

    def convert_decimal_to_16_bit(self, decimal):
        result = list(str(bin(decimal)))[2:]
        empty_instruction = ["0" for x in range(16)]
        for x in range(min(len(result), 16)):
            empty_instruction[-x - 1] = result[-x - 1]
        
        return ''.join(empty_instruction)

    def convert_decimal_list_to_16_bit(self, list_decimal):
        ret = []
        for x in list_decimal:
            ret.append(self.convert_decimal_to_16_bit(x))
        
        return ret


    def translate_jack_program_to_binary(self, program):
        lol = comp_engine(program)
        lol.match_jack_program()
        vm = Vm()

        assembly_instructions= vm.get_hack_assembly_instructions_from_VM_instructions(lol.vm_program.VM_commands_list)
        ass = assembler()
        return ass.array_hack_assembly_instruction_to_binary_instruction(assembly_instructions)



    def test_simple_assignment_seven(self):
        seven_program = """
            class Main_Class {
                static int i;
                function void main() {
                    let i = (3 + 2 - 2) + 1 - (2 - 5);
                    return null;
                }
            }
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(seven_program))
        comp.run_N_number_instructions(1000)

        self.assertEqual(self.convert_decimal_to_16_bit(7), comp.data_memory.memory[16])

    def test_simple_if_statement_assignment(self):
        program = """
            class Main_Class {
                static int i, j, x, y;
                function void main() {
                    if (923 > 120) {
                        let i = 911;
                        let j = 420;
                    } else {
                        let i = 8008;
                        let j = 69;
                    }

                    if (1111 - 5 < 5) {
                        let x = 12;
                        let y = 21920;
                    } else {
                        let x = 1406;
                        let y = 5736;
                    }
                    
                }
            }
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(program))
        comp.run_N_number_instructions(1000)

        self.assertEqual(self.convert_decimal_list_to_16_bit([911, 420, 1406, 5736]), comp.data_memory.memory[16:20])


if __name__ == '__main__':
    unittest.main()