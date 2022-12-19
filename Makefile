run_test: test
	python3 test/test_gates.py
	python3 test/test_alu.py
	python3 test/test_sequential_logic.py
	python3 test/test_cpu.py
	
run: src/main.py
	python3 src/main.py

gui_run: src/GUI.py
	python3 src/GUI.py