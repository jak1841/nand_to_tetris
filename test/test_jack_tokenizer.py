import unittest
from Jack_tokenizer import tokenizer as tk

class Test(unittest.TestCase):
    # jack program found in elements in computing systems page 258
    def test_square_class_code_tokenizer(self):
        jack_program = """
        /* Increases the size of the method lol */
            method void incSize() {
                if (((y + size) < 254)) &
                    ((x + size) < 510) {
                    do erase();
                    let size = size + 2;
                    do draw();
                }
                return;
            }"""

        tokenizer_jack_program = tk(jack_program)

        expected_token_list = [("method", "keyword"), ("void", "keyword"), ("incSize", "identifier"), 
        ("(", "symbol"), (")", "symbol"), ("{", "symbol"), ("if", "keyword"), ("(", "symbol"), ("(", "symbol"), 
        ("(", "symbol"), ("y", "identifier"), ("+", "symbol"), ("size", "identifier"), (")", "symbol"), 
        ("<", "symbol"), ("254", "integerConstant"), (")", "symbol"), (")", "symbol"), ("&", "symbol"), 
        ("(", "symbol"), ("(", "symbol"), ("x", "identifier"), ("+", "symbol"), ("size", "identifier"), 
        (")", "symbol"), ("<", "symbol"), ("510", "integerConstant"), (")", "symbol"), ("{", "symbol"), 
        ("do", "keyword"), ("erase", "identifier"), ("(", "symbol"), (")", "symbol"), (";", "symbol"), 
        ("let", "keyword"), ("size", "identifier"), ("=", "symbol"), ("size", "identifier"), ("+", "symbol"), 
        ("2", "integerConstant"), (";", "symbol"), ("do", "keyword"), ("draw", "identifier"), ("(", "symbol"), 
        (")", "symbol"), (";", "symbol"), ("}", "symbol"), ("return", "keyword"), (";", "symbol"), ("}", "symbol")]

        self.assertEqual(expected_token_list, tokenizer_jack_program.get_all_tokens())

    def test_expressionless_square_class_code_tokenizer(self):
        jack_program = """
            method void incSize() {
                if (x) {
                    do erase();
                    let size=size;
                    do draw();
                }
                return;
            }
            """

        tokenizer_jack_program = tk(jack_program)
        expected_token_list = [("method", "keyword"), ("void", "keyword"), ("incSize", "identifier"), ("(", "symbol"), (")", "symbol"), 
        ("{", "symbol"), ("if", "keyword"), ("(", "symbol"), ("x", "identifier"), (")", "symbol"), ("{", "symbol"), ("do", "keyword"), 
        ("erase", "identifier"), ("(", "symbol"), (")", "symbol"), (";", "symbol"), ("let", "keyword"), ("size", "identifier"), ("=", "symbol"), 
        ("size", "identifier"), (";", "symbol"), ("do", "keyword"), ("draw", "identifier"), ("(", "symbol"), 
        (")", "symbol"), (";", "symbol"), ("}", "symbol"), ("return", "keyword"), (";", "symbol"), ("}", "symbol")]

        self.assertEqual(expected_token_list, tokenizer_jack_program.get_all_tokens())

    def test_Array_average_code_tokenizer(self):
        jack_program = """
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
            """
        tokenizer_jack_program = tk(jack_program)
        expected_token_list = [("method", "keyword"), ("int", "keyword"), ("average", "identifier"), ("(", "symbol"), ("Array", "identifier"), 
        ("numbers", "identifier"), (",", "symbol"), ("int", "keyword"), ("array_length", "identifier"), (")", "symbol"), ("{", "symbol"), 
        ("var", "keyword"), ("int", "keyword"), ("sum", "identifier"), (";", "symbol"), ("var", "keyword"), ("int", "keyword"), 
        ("index", "identifier"), (";", "symbol"), ("let", "keyword"), ("index", "identifier"),  ("=", "symbol"), ("0", "integerConstant"), 
        (";", "symbol"), ("let", "keyword"), ("sum", "identifier"),  ("=", "symbol"), ("0", "integerConstant"), (";", "symbol"), 
        ("while", "keyword"), ("(", "symbol"), ("index", "identifier"), ("<", "symbol"), ("array_length", "identifier"), (")", "symbol"), 
        ("{", "symbol"), ("let", "keyword"), ("sum", "identifier"),  ("=", "symbol"), ("sum", "identifier"), ("+", "symbol"), ("numbers", "identifier"), 
        ("[", "symbol"),  ("index", "identifier"), ("]", "symbol"), (";", "symbol"), 

        ("let", "keyword"), ("index", "identifier"),  ("=", "symbol"), ("index", "identifier"), ("+", "symbol"), ("1", "integerConstant"), 
        (";", "symbol"), ("}", "symbol"), ("return", "keyword"), ("(", "symbol"), ("sum", "identifier"), ("/", "symbol"), ("array_length", "identifier"), 
        (")", "symbol"), (";", "symbol"), ("}", "symbol")
        ]

        self.assertEqual(expected_token_list, tokenizer_jack_program.get_all_tokens())




if __name__ == '__main__':
    unittest.main()