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

    def test_simple_while_statement(self):
        program = """
            class Main_Class {
                static int i, j, k;
                function int main() {
                    while (i < 50) {
                        let j = j + i;
                        let i = i + 1;
                    }

                    while (i < 100) {
                        let k = k + 3;
                        let i = i + 1;
                    }

                    return 0;

                }

                
            }
        
        
        """
        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(program))
        comp.run_N_number_instructions(18000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([100, 1225, 150]), comp.data_memory.memory[16:19])

    def test_simple_function_calling(self):
        program = """
            class Main_Class {
                static int i;
                static int j;

                /* Given two positive ints return there product */
                function int multiply(int x, int y) {
                    var int return_product;

                    let return_product = 0;

                    while (y > 0) {
                        let return_product = return_product + x;
                        let y = y - 1;
                    }

                    return return_product;

                } 

                function int main() {
                    let i = Main_Class.multiply(200, 128);
                    do Main_Class.add_unknown_number(0);
                    do Main_Class.add_unknown_number(1);
                    do Main_Class.add_unknown_number(2);
                    do Main_Class.add_unknown_number(3);
                    do Main_Class.add_unknown_number(4);

                    let j = Main_Class.add_unknown_number(20);

                    return 0;
                }

                function int add_unknown_number(int x) {
                    return x + 69;
                }
            }
        
        """
        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(program))
        comp.run_N_number_instructions(30000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([25600, 89]), comp.data_memory.memory[16:18])

    def test_recursive_function_calling(self):
        program = """
            class Main_Class {
                static int i;

                /* Given two positive ints return there product */
                function int multiply(int x, int y) {
                    var int return_product;

                    let return_product = 0;

                    while (y > 0) {
                        let return_product = return_product + x;
                        let y = y - 1;
                    }

                    return return_product;

                } 

                function int do_recursive_operation(int x) {
                    if (x = 0) {
                        return 1;
                    } else {
                        return Main_Class.multiply(x, Main_Class.do_recursive_operation(x - 1));
                    }
                }

                function int main() {
                    let i = Main_Class.do_recursive_operation(6);
                    return 0;
                }
            }
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(program))
        comp.run_N_number_instructions(40000)
        self.assertEqual(self.convert_decimal_to_16_bit(720), comp.data_memory.memory[16])


if __name__ == '__main__':
    unittest.main()