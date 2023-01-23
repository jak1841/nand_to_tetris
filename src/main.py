from Jack_tokenizer import tokenizer as tk

jack_program = """

if (x < 153)
    {let city="Paris";}

"""

l = tk(jack_program)

l.print_all_tokens_fxml()






