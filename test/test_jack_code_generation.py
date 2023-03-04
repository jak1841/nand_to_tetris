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
        if (decimal == -1):
            return "1111111111111111"
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

    def translate_jack_program_to_binary_with_libraries(self, program):
        lol = comp_engine(program)
        lol.add_all_libraries_to_tokens()
        lol.match_jack_program()
        vm = Vm()
        assembly_instructions= vm.get_hack_assembly_instructions_from_VM_instructions(lol.vm_program.VM_commands_list)
        ass = assembler()
        return ass.array_hack_assembly_instruction_to_binary_instruction(assembly_instructions)

    def test_conditionals(self):
        program = """
            class Main_Class {
                
                function int get_temperature () {
                    return 11;
                }

                function void main() {
                    var int x, y;
                    let x = 1;
                    let y = 1;
                    do Memory.init();
                    do Memory.poke(800, (7 < 8));
                    do Memory.poke(801, (8 < 7));
                    do Memory.poke(802, (false | true));
                    do Memory.poke(803, (true & true));
                    do Memory.poke(804, (8 = 8));
                    do Memory.poke(805, (Main_Class.get_temperature() > 10));
                    do Memory.poke(806, (Main_Class.get_temperature() < 10));
                    do Memory.poke(807, (Main_Class.get_temperature() = 10));
                    do Memory.poke(808, (Main_Class.get_temperature() = 11));
                    do Memory.poke(809, (1 < 4) & (4 < 8));
                    do Memory.poke(810, (8 = 7) | (-7 = -7));
                    do Memory.poke(811, (1 < -1));
                    do Memory.poke(812, (y = x));
 
                    return null;
                }
            }
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(5000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([-1, 0, -1, -1, -1, -1, 0, 0, -1, -1, -1 , 0, -1]), comp.data_memory.memory[800:813])

    def test_multiplication(self):
        program = """
            class Main_Class {
                function void main() {
                    do Memory.init();
                    do Memory.poke(800, 2*3);
                    do Memory.poke(801, 0*1);
                    do Memory.poke(802, 9212*1);
                    do Memory.poke(803, 83*219);
                    do Memory.poke(804, 9999* 6);
                    return null;
                }
            }
        """
                
        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(5000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([6, 0, 9212, 18177, 59994]), comp.data_memory.memory[800:805])

    def test_division(self):
        program = """
            class Main_Class {
                function void main() {
                    do Memory.init();
                    do Memory.poke(800, 100/5);
                    do Memory.poke(801, 72/9);
                    do Memory.poke(802, (-911)/911);
                    
                    return null;
                }
            }
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(2000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([20, 8, -1]), comp.data_memory.memory[800:803])

    def test_sqrt(self):
        program = """
            class Main_Class {
                function void main() {
                    do Memory.init();
                    do Memory.poke(800, Math.sqrt(100));
                    do Memory.poke(801, Math.sqrt(4));
                    do Memory.poke(802, Math.sqrt(2));
                    
                    return null;
                }
            }
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(30000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([10, 2, 1]), comp.data_memory.memory[800:803])
       


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
                    var int t1, t2;
                    
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


                    return 0;
                    
                    
                }
            }
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary(program))
        comp.run_N_number_instructions(10000)

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

                    while (i > 2000) {
                        let k = k + 10000;
                    }

                    while (false) {
                        let k = k + 1000;
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

    def test_basic_object_implementation(self):
        program = """
            class Point {
                field int x, y;
                constructor Point new(int x1, int y1) {
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

                /* Given another pt returns true if x is greater */
                function int is_point_x_greater (Point p) {
                    return (p.get_x() < x);
                }

                function int is_point_y_greater (Point p) {
                    return (y > p.get_y());
                }

            }

            class Main_Class {
                static int p1x, p1y, p2x, p2y, is_greater_x, is_greater_y;
                function int main () {
                    var Point p1, p2;
                                
                    do Memory.init();

                    let p1 = Point.new(7, 8);
                    let p2 = Point.new(15, 16);

                    let p1x = p1.get_x();
                    let p1y = p1.get_y();
                    let p2x = p2.get_x();
                    let p2y = p2.get_y();
                    
                    let is_greater_x = p2.is_point_x_greater(p1);
                    let is_greater_y = p1.is_point_y_greater(p2);

                    return null;
                }
            }

        
        
        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(10000)

        self.assertEqual(self.convert_decimal_list_to_16_bit([7, 8, 15, 16, -1, 0]), comp.data_memory.memory[16:22])

        # self.assertEqual(self.convert_decimal_list_to_16_bit([2, 7, 8, 20, 0]), comp.data_memory.memory[16:21])

    def test_linked_list_implementation_using_objects(self):
        program = """
            class Node {
                field Node next;
                field int is_tail;
                field int number;

                constructor Node new(int value) {
                    let is_tail = true;
                    let number = value;
                    return this;
                }

                function int add_next_node(int value) {
                    let next = Node.new(value);
                    let is_tail = false;
                    return 0;
                }

                function Node get_next_node() {
                    return next;
                }

                function int get_number() {
                    return number;
                }

                function int get_is_tail() {
                    return is_tail;
                }
                



            }

            class Main_Class {
                function int main () {
                    var Node head, cur;
                    var int i;

                    do Memory.init();

                    let head = Node.new(0);
                    let cur = head;
                    let i = 1;

                    while (i < 17) {
                        do cur.add_next_node(i);
                        let cur = cur.get_next_node();
                        let i = i + 1;
                    }

                    let cur = head;
                    let i = 0;
                    while (cur.get_is_tail() = false) {
                        do Memory.poke(800 + i, cur.get_number());
                        let cur = cur.get_next_node();
                        let i = i + 1;
                    }
                    return null;
                }
            }

        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(50000)
        self.assertEqual(self.convert_decimal_list_to_16_bit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]), comp.data_memory.memory[800:817])

    def test_decimal_to_binary_conversion(self):
        # Stores a decimal in RAM[8000] and then converts that into binary and stores in RAM[8001-8016] as eithier 0 or 1 
        program = """
            class Main_Class {
                static int pos;
                function int main () {
                    do Main_Class.init_ram_8000(63);
                    
                    return null;
                }

                /* Given a decimal number stores in ram 8000 and also initializes all ram locations after that with -1*/
                function int init_ram_8000(int decimal) {
                    var int i;
                    do Memory.poke(8000, decimal);
                    let i = 8001; 

                    while (i < 8017) {
                        do Memory.poke(i, -1);
                        let i = i + 1;
                    }
                    return null;
                }



            }

        """

        comp = computer()
        comp.load_program(self.translate_jack_program_to_binary_with_libraries(program))
        comp.run_N_number_instructions(10000)
        


if __name__ == '__main__':
    unittest.main()