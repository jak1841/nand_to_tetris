import unittest
from Jack_compilation_engine import comp_engine 

class Test(unittest.TestCase):
    def test_bank_account(self):
        jack_bank_account_code = """
        /* Some common sense was sacrificed in this banking example in order to 
           create a nontrivial and easy-to-follow compilation example. */

        class BankAccount {
            /* Class variables */
            static int nAccounts; 
            static int bankCommission; /* As a percentage, e.g., 10 for 10 percent*/
            /* account properties */
            field int id; 
            field String owner;
            field int balance;

            method int comission (int x) {/* Code omitted */}

            method void transfer (int sum, BankAccount from, Date when) {
                var int i, j; /* Some local variables */
                var Date due; /* Date is a user-defined type */
                let balance = (balance + sum) - comission(sum * 5);
                /* More code ...*/
                return;
            }

            /* More methods */
        }
        """
        lol = comp_engine(jack_bank_account_code)

        lol.match_class()
        class_variable_names = ["nAccounts", "bankCommission", "id", "owner", "balance"]
        class_variable_type_kind_index = [("int", "STATIC", 0), ("int", "STATIC", 1), ("int", "FIELD", 0), ("String", "FIELD", 1), ("int", "FIELD", 2) ]

        subroutine_variables_names = ["sum", "from", "when", "i", "j", "due"]
        subroutine_variables_type_kind_index = [("int", "ARG", 0), ("BankAccount", "ARG", 1), ("Date", "ARG", 2), ("int", "VAR", 0 ), ("int", "VAR", 1 ), ("Date", "VAR", 2 )]
        for x in range(len(class_variable_names)):
            self.assertEqual(lol.symbol_table.class_symbol_table[class_variable_names[x]], class_variable_type_kind_index[x])

        for x in range(len(subroutine_variables_names)):
            self.assertEqual(lol.symbol_table.subroutine_symbol_table[subroutine_variables_names[x]], subroutine_variables_type_kind_index[x])


if __name__ == '__main__':
    unittest.main()