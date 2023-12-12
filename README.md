# Reproducing the bug

1. Create a python virtual environment, using the suggested directory name: `python3 -m venv .testvenv`.
1. Activate the environment: `. .testvenv/bin/activate`.
1. Select the environment as the source for the interpreter to be used in VSCode via `Python: Select Interpreter`.
1. Run the tests in VSCode via `Test: Run All Tests`.
   **Problem: The tests fail, but they should pass.**
1. To see that the tests pass as expected when running the tests in debug mode, run `Test: Debug All Tests`.
