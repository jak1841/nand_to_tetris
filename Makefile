run_test: test
	python3 test/test_gates.py
	python3 test/test_alu.py
	python3 test/test_sequential_logic.py
	
run: src/main.py
	python3 src/main.py

