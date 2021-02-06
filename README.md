# Python Apptitude Test
Read the instructions on all test[0-5].py and complete the code. Run `pytest -v` to see if your code is written correctly.

Good luck!

## Rules
- Complete the tests within 30 minutes. Run `pytest -v` to see results.
- Internet access is restricted to only Python keywords search (e.g. sum, range etc). Search on the instructions is not allowed.

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Test Driven Development (TDD)
This test also demonstrate the test-first approach in TDD.
1. Write the test code with hardcoded inputs with its expected corresponding output.
1. Create the skeleton code and comments without the logic. It could be just a simple empty function or method.
1. RED: make the test fail by returning a wrong value in step 1.
1. GREEN: make the test pass by returning a correct hardcoded value in step 1.
1. BLUE: write the actual code.