	

run_cur_test: test
	pypy test/test_gates.py
	pypy test/test_alu.py
	pypy test/test_sequential_logic.py
	pypy test/test_cpu.py
	pypy test/test_assembler.py
	pypy test/test_draw_rect.py
	pypy test/test_jack_tokenizer.py
	
all_tests_run: test
	pypy test/test_gates.py
	pypy test/test_alu.py
	pypy test/test_sequential_logic.py
	pypy test/test_cpu.py
	pypy test/test_assembler.py
	pypy test/test_draw_rect.py
	pypy test/test_vm_instructions.py
	pypy test/test_jack_tokenizer.py



slow_run: src/main.py
	python3 src/main.py

fast_run: src/main.py
	pypy src/main.py

gui_run: src/GUI.py
	python3 src/GUI.py

