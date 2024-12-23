export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)

PC = pypy3
PC_SLOW = python3

run_cur_test: test
	$(PC) test/test_gates.py
	$(PC) test/test_alu.py
	$(PC) test/test_sequential_logic.py
	$(PC) test/test_cpu.py
	$(PC) test/test_assembler.py
	$(PC) test/test_draw_rect.py
	$(PC) test/test_jack_tokenizer.py
	$(PC) test/test_jack_syntax_analyzer.py
	$(PC) test/test_symbol_table.py
	$(PC) test/test_jack_code_generation.py
	
	
all_tests_run: test
	$(PC) test/test_gates.py
	$(PC) test/test_alu.py
	$(PC) test/test_sequential_logic.py
	$(PC) test/test_cpu.py
	$(PC) test/test_assembler.py
	$(PC) test/test_draw_rect.py
	$(PC) test/test_vm_instructions.py
	$(PC) test/test_jack_tokenizer.py
	$(PC) test/test_jack_syntax_analyzer.py
	$(PC) test/test_symbol_table.py
	$(PC) test/test_jack_code_generation.py



slow_run: src/main.py
	$(PC_SLOW) src/main.py

fast_run: src/main.py
	$(PC) src/main.py

gui_run: src/GUI.py
	$(PC_SLOW) src/GUI.py

