import unittest
from central_processing_unit import cpu_16_bit
from hack_assembler import assembler

assem = assembler()

class Test(unittest.TestCase):
    def test_cpu_comp_operation(self):
        cpu = cpu_16_bit()

        # Initial Register and PC test 
        self.assertEqual(0000000000000000, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0000000000000000, cpu.D_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0000000000000000, cpu.PC.register_16_bit(0000000000000000, 0))

        # 0
        inM, reset = 0000000000000000, 0
        instruction = assem.convertAssemblyToBinary("null=0;null")
        self.assertEqual([0000000000000000, 0, 0000000000000000, 0b0000000000000001], cpu.execute_instruction(inM, instruction, reset))
        
        # 1
        inM, reset = 0000000000000000, 0
        instruction = assem.convertAssemblyToBinary("null=1;null")
        self.assertEqual([0b0000000000000001, 0, 0b0000000000000000, 0b0000000000000010], cpu.execute_instruction(inM, instruction, reset))

        # -1
        inM, reset = 0000000000000000, 0
        instruction = assem.convertAssemblyToBinary("null=-1;null")
        self.assertEqual([0b1111111111111111, 0, 0000000000000000, 0b0000000000000011], cpu.execute_instruction(inM, instruction, reset))

        # Assigning values to the game
        inM, reset = 0000000000000000, 0
        instruction = assem.convertAssemblyToBinary("@169")
        cpu.execute_instruction(inM, instruction, reset)
        instruction = assem.convertAssemblyToBinary("D=A;null")
        cpu.execute_instruction(inM, instruction, reset)
        instruction = assem.convertAssemblyToBinary("@911")
        cpu.execute_instruction(inM, instruction, reset)
        self.assertEqual(0b0000001110001111, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000010101001, cpu.D_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000000000110, cpu.PC.register_16_bit(0000000000000000, 0))

        # D
        inM, reset = 0000000000000000, 0
        instruction = assem.convertAssemblyToBinary("null=D;null")
        self.assertEqual([0b0000000010101001, 0, 0b0000001110001111, 0b0000000000000111], cpu.execute_instruction(inM, instruction, reset))


        # A
        instruction = assem.convertAssemblyToBinary("null=A;null")
        self.assertEqual([0b0000001110001111, 0, 0b0000001110001111, 0b0000000000001000], cpu.execute_instruction(inM, instruction, reset))

        # !D
        instruction = assem.convertAssemblyToBinary("null=!D;null")
        self.assertEqual([0b1111111101010110, 0, 0b0000001110001111, 0b0000000000001001], cpu.execute_instruction(inM, instruction, reset))

        # !A
        instruction = assem.convertAssemblyToBinary("null=!A;null")
        self.assertEqual([0b1111110001110000, 0, 0b0000001110001111, 0b0000000000001010], cpu.execute_instruction(inM, instruction, reset))

        # -D
        instruction = assem.convertAssemblyToBinary("null=-D;null")
        self.assertEqual([0b1111111101010111, 0, 0b0000001110001111, 0b0000000000001011], cpu.execute_instruction(inM, instruction, reset))

        # -A
        instruction = assem.convertAssemblyToBinary("null=-A;null")
        self.assertEqual([0b1111110001110001, 0, 0b0000001110001111, 0b0000000000001100], cpu.execute_instruction(inM, instruction, reset))

        # D+1
        instruction = assem.convertAssemblyToBinary("null=D+1;null")
        self.assertEqual([0b0000000010101010, 0, 0b0000001110001111, 0b0000000000001101], cpu.execute_instruction(inM, instruction, reset))

        # A+1
        instruction = assem.convertAssemblyToBinary("null=A+1;null")
        self.assertEqual([0b0000001110010000, 0, 0b0000001110001111, 0b0000000000001110], cpu.execute_instruction(inM, instruction, reset))

        # D-1
        instruction = assem.convertAssemblyToBinary("null=D-1;null")
        self.assertEqual([0b0000000010101000, 0, 0b0000001110001111, 0b0000000000001111], cpu.execute_instruction(inM, instruction, reset))

        # A-1
        instruction = assem.convertAssemblyToBinary("null=A-1;null")
        self.assertEqual([0b0000001110001110, 0, 0b0000001110001111, 0b0000000000010000], cpu.execute_instruction(inM, instruction, reset))

        # D+A
        instruction = assem.convertAssemblyToBinary("null=D+A;null")
        self.assertEqual([0b0000010000111000, 0, 0b0000001110001111, 0b0000000000010001], cpu.execute_instruction(inM, instruction, reset))

        # D-A
        instruction = assem.convertAssemblyToBinary("null=D-A;null")
        self.assertEqual([0b1111110100011010, 0, 0b0000001110001111, 0b0000000000010010], cpu.execute_instruction(inM, instruction, reset))

        # A-D
        instruction = assem.convertAssemblyToBinary("null=A-D;null")
        self.assertEqual([0b0000001011100110, 0, 0b0000001110001111, 0b0000000000010011], cpu.execute_instruction(inM, instruction, reset))

        # D&A
        instruction = assem.convertAssemblyToBinary("null=D&A;null")
        self.assertEqual([0b0000000010001001, 0, 0b0000001110001111, 0b0000000000010100], cpu.execute_instruction(inM, instruction, reset))

        # D|A
        instruction = assem.convertAssemblyToBinary("null=D|A;null")
        self.assertEqual([0b0000001110101111, 0, 0b0000001110001111, 0b0000000000010101], cpu.execute_instruction(inM, instruction, reset))



        inM, reset = 0b1101011010011111, 0
        # M 
        instruction = assem.convertAssemblyToBinary("null=M;null")
        self.assertEqual([0b1101011010011111, 0, 0b0000001110001111, 0b0000000000010110], cpu.execute_instruction(inM, instruction, reset))

        # !M
        instruction = assem.convertAssemblyToBinary("null=!M;null")
        self.assertEqual([0b0010100101100000, 0, 0b0000001110001111, 0b0000000000010111], cpu.execute_instruction(inM, instruction, reset))

        # -M
        instruction = assem.convertAssemblyToBinary("null=-M;null")
        self.assertEqual([0b0010100101100001, 0, 0b0000001110001111, 0b0000000000011000], cpu.execute_instruction(inM, instruction, reset))

        # M+1
        instruction = assem.convertAssemblyToBinary("null=M+1;null")
        self.assertEqual([0b1101011010100000, 0, 0b0000001110001111, 0b0000000000011001], cpu.execute_instruction(inM, instruction, reset))

        # M-1
        instruction = assem.convertAssemblyToBinary("null=M-1;null")
        self.assertEqual([0b1101011010011110, 0, 0b0000001110001111, 0b0000000000011010], cpu.execute_instruction(inM, instruction, reset))

        # D+M
        instruction = assem.convertAssemblyToBinary("null=D+M;null")
        self.assertEqual([0b1101011101001000, 0, 0b0000001110001111, 0b0000000000011011], cpu.execute_instruction(inM, instruction, reset))

        # D-M
        instruction = assem.convertAssemblyToBinary("null=D-M;null")
        self.assertEqual([0b0010101000001010, 0, 0b0000001110001111, 0b0000000000011100], cpu.execute_instruction(inM, instruction, reset))

        # M-D
        instruction = assem.convertAssemblyToBinary("null=M-D;null")
        self.assertEqual([0b1101010111110110, 0, 0b0000001110001111, 0b0000000000011101], cpu.execute_instruction(inM, instruction, reset))

        # D&M
        instruction = assem.convertAssemblyToBinary("null=D&M;null")
        self.assertEqual([0b0000000010001001, 0, 0b0000001110001111, 0b0000000000011110], cpu.execute_instruction(inM, instruction, reset))

        # D|M
        instruction = assem.convertAssemblyToBinary("null=D|M;null")
        self.assertEqual([0b1101011010111111, 0, 0b0000001110001111, 0b0000000000011111], cpu.execute_instruction(inM, instruction, reset))

    def test_cpu_store_operation(self):
        cpu = cpu_16_bit()
        self.assertEqual(0000000000000000, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0000000000000000, cpu.D_register.register_16_bit(0000000000000000, 0))

        inM, reset = 0b1110101000000000, 0
        instruction = assem.convertAssemblyToBinary("@993")
        cpu.execute_instruction(inM, instruction, reset)

        self.assertEqual(0b0000001111100001, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0000000000000000, cpu.D_register.register_16_bit(0000000000000000, 0))

        instruction = assem.convertAssemblyToBinary("D=A;null")
        cpu.execute_instruction(inM, instruction, reset)

        instruction = assem.convertAssemblyToBinary("@21902")
        cpu.execute_instruction(inM, instruction, reset)
    
        self.assertEqual(0b0101010110001110, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000001111100001, cpu.D_register.register_16_bit(0000000000000000, 0))


        instruction = assem.convertAssemblyToBinary("M=A;null")
        self.assertEqual([0b0101010110001110, 1, 0b0101010110001110, 0b0000000000000100], cpu.execute_instruction(inM, instruction, reset))
    
        self.assertEqual(0b0101010110001110, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000001111100001, cpu.D_register.register_16_bit(0000000000000000, 0))
        


        instruction = assem.convertAssemblyToBinary("D=D+1;null")
        self.assertEqual([0b0000001111100010, 0, 0b0101010110001110, 0b0000000000000101], cpu.execute_instruction(inM, instruction, reset))
    
        self.assertEqual(0b0101010110001110, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000001111100010, cpu.D_register.register_16_bit(0000000000000000, 0))

        inM = 0b0101010110001110
        instruction = assem.convertAssemblyToBinary("MD=D&A;null")
        self.assertEqual([0b0000000110000010, 1, 0b0101010110001110, 0b0000000000000110], cpu.execute_instruction(inM, instruction, reset))
    
        self.assertEqual(0b0101010110001110, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000110000010, cpu.D_register.register_16_bit(0000000000000000, 0))


        inM = 0b1101010110001110
        instruction = assem.convertAssemblyToBinary("A=A+1;null")
        self.assertEqual([0b0101010110001111, 0, 0b0101010110001111, 0b0000000000000111], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0101010110001111, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000110000010, cpu.D_register.register_16_bit(0000000000000000, 0))

        instruction = assem.convertAssemblyToBinary("AM=D|M;null")
        self.assertEqual([0b1101010110001110, 1, 0b1101010110001110, 0b0000000000001000], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b1101010110001110, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000110000010, cpu.D_register.register_16_bit(0000000000000000, 0))


        inM = 0b1111110000000111
        instruction = assem.convertAssemblyToBinary("AD=M;null")
        self.assertEqual([0b1111110000000111, 0, 0b1111110000000111, 0b0000000000001001], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b1111110000000111, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b1111110000000111, cpu.D_register.register_16_bit(0000000000000000, 0))


        inM = 0b1111110000000111
        instruction = assem.convertAssemblyToBinary("AMD=1;null")
        self.assertEqual([0b0000000000000001, 1, 0b0000000000000001, 0b0000000000001010], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0000000000000001, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000000000001, cpu.D_register.register_16_bit(0000000000000000, 0))
        
    def test_cpu_jump_operation(self):
        cpu = cpu_16_bit()
        inM, reset = 0000000000000000, 0

        instruction = assem.convertAssemblyToBinary("null=0;null")
        self.assertEqual([0000000000000000, 0, 0000000000000000, 0b0000000000000001], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0000000000000000, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000000000001, cpu.PC.register_16_bit(0000000000000000, 0))



        instruction = assem.convertAssemblyToBinary("@1802")
        self.assertEqual([0b1111111111111111, 0, 0b0000011100001010, 0b0000000000000010], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0000011100001010, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000000000010, cpu.PC.register_16_bit(0000000000000000, 0))


        # !JEQ
        instruction = assem.convertAssemblyToBinary("D=1;JEQ")
        self.assertEqual([0b0000000000000001, 0, 0b0000011100001010, 0b0000000000000011], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0000011100001010, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000000000000011, cpu.PC.register_16_bit(0000000000000000, 0))

        # JEQ
        instruction = assem.convertAssemblyToBinary("D=D-1;JEQ")
        self.assertEqual([0000000000000000, 0, 0b0000011100001010, 0b0000011100001010], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0000011100001010, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000011100001010, cpu.PC.register_16_bit(0000000000000000, 0))

        # !JGT
        instruction = assem.convertAssemblyToBinary("D=D;JGT")
        self.assertEqual([0000000000000000, 0, 0b0000011100001010, 0b0000011100001011], cpu.execute_instruction(inM, instruction, reset))
        self.assertEqual(0b0000011100001010, cpu.A_register.register_16_bit(0000000000000000, 0))
        self.assertEqual(0b0000011100001011, cpu.PC.register_16_bit(0000000000000000, 0))

        # !JGT 
        instruction = assem.convertAssemblyToBinary("null=D-1;JGT")
        self.assertEqual([0b1111111111111111, 0, 0b0000011100001010, 0b0000011100001100], cpu.execute_instruction(inM, instruction, reset))


        instruction = assem.convertAssemblyToBinary("@9210")
        cpu.execute_instruction(inM, instruction, reset)


        # JGT
        instruction = assem.convertAssemblyToBinary("null=1;JGT")
        self.assertEqual([0b0000000000000001, 0, 0b0010001111111010, 0b0010001111111010], cpu.execute_instruction(inM, instruction, reset))

        # !JGE
        instruction = assem.convertAssemblyToBinary("null=D-1;JGE")
        self.assertEqual([0b1111111111111111, 0, 0b0010001111111010, 0b0010001111111011], cpu.execute_instruction(inM, instruction, reset))

        # JGE
        instruction = assem.convertAssemblyToBinary("null=0;JGE")
        self.assertEqual([0b0000000000000000, 0, 0b0010001111111010, 0b0010001111111010], cpu.execute_instruction(inM, instruction, reset))

        # JGE
        instruction = assem.convertAssemblyToBinary("null=1;JGE")
        self.assertEqual([0b0000000000000001, 0, 0b0010001111111010, 0b0010001111111010], cpu.execute_instruction(inM, instruction, reset))

        # !JLT 
        instruction = assem.convertAssemblyToBinary("null=0;JLT")
        self.assertEqual([0b0000000000000000, 0, 0b0010001111111010, 0b0010001111111011], cpu.execute_instruction(inM, instruction, reset))

        # !JLT 
        instruction = assem.convertAssemblyToBinary("null=1;JLT")
        self.assertEqual([0b0000000000000001, 0, 0b0010001111111010, 0b0010001111111100], cpu.execute_instruction(inM, instruction, reset))

        # JLT
        instruction = assem.convertAssemblyToBinary("null=D-1;JLT")
        self.assertEqual([0b1111111111111111, 0, 0b0010001111111010, 0b0010001111111010], cpu.execute_instruction(inM, instruction, reset))

        instruction = assem.convertAssemblyToBinary("@2002")
        cpu.execute_instruction(inM, instruction, reset)

        # !JNE 
        instruction = assem.convertAssemblyToBinary("null=0;JNE")
        self.assertEqual([0000000000000000, 0, 0b0000011111010010, 0b0010001111111100], cpu.execute_instruction(inM, instruction, reset))

        # JNE
        instruction = assem.convertAssemblyToBinary("null=1;JNE")
        self.assertEqual([0b0000000000000001, 0, 0b0000011111010010, 0b0000011111010010], cpu.execute_instruction(inM, instruction, reset))

        # JNE 
        instruction = assem.convertAssemblyToBinary("null=D-1;JNE")
        self.assertEqual([0b1111111111111111, 0, 0b0000011111010010, 0b0000011111010010], cpu.execute_instruction(inM, instruction, reset))

        instruction = assem.convertAssemblyToBinary("@60000")
        cpu.execute_instruction(inM, instruction, reset)
        

        # !JLE
        instruction = assem.convertAssemblyToBinary("null=1;JLE")
        self.assertEqual([0b0000000000000001, 0, 0b0110101001100000, 0b0000011111010100], cpu.execute_instruction(inM, instruction, reset))

        # JLE
        instruction = assem.convertAssemblyToBinary("null=0;JLE")
        self.assertEqual([0000000000000000, 0, 0b0110101001100000, 0b0110101001100000], cpu.execute_instruction(inM, instruction, reset))

        # JLE
        instruction = assem.convertAssemblyToBinary("null=D-1;JLE")
        self.assertEqual([0b1111111111111111, 0, 0b0110101001100000, 0b0110101001100000], cpu.execute_instruction(inM, instruction, reset))


        instruction = assem.convertAssemblyToBinary("@32000")
        cpu.execute_instruction(inM, instruction, reset)

        

        # JMP 
        instruction = assem.convertAssemblyToBinary("null=D-1;JMP")
        self.assertEqual([0b1111111111111111, 0, 0b0111110100000000, 0b0111110100000000], cpu.execute_instruction(inM, instruction, reset))

        instruction = assem.convertAssemblyToBinary("null=1;JMP")
        self.assertEqual([0b0000000000000001, 0, 0b0111110100000000, 0b0111110100000000], cpu.execute_instruction(inM, instruction, reset))

        instruction = assem.convertAssemblyToBinary("null=0;JMP")
        self.assertEqual([0000000000000000, 0, 0b0111110100000000, 0b0111110100000000], cpu.execute_instruction(inM, instruction, reset))


        # Reset 
        reset = 1
        instruction = assem.convertAssemblyToBinary("null=D-1;JMP")
        self.assertEqual([0b1111111111111111, 0, 0b0111110100000000, 0000000000000000], cpu.execute_instruction(inM, instruction, reset))







        

        

        





if __name__ == '__main__':
    unittest.main()