# Python Unit Testing
The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for Python applications. This tutorial aims to help learners to get started with Test Driven Development (TDD) in Python.

## Git Clone
Git clone this repo into your project folder.

## Setup
Change to the repo directory using `cd python-unit-testing`.

For Linux and MacOS
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

For Windows
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Project Structure
```
/app (main app dir)
  |__ test (unit tests)
```
Each python code file would correspond with a test file under `/test` e.g. `app/test0.py` with `app/test/test_test0.py` etc.

## Running Pytest
To run a single test:
`pytest -v app/test/test_test[*].py`

To run all tests with code coverage report:
`pytest -v --cov=app`

## Steps in Unit Testings
1. Add a test under the `app/test` directory
1. Fail the test
1. Write the simplest code to pass test
1. Pass the test
1. Refactor code as needed
1. Repeat above steps until every requirement is done

## Python Unit Test Cheat Sheet
Download a [PDF cheat sheet for Beginners](https://edu.anarcho-copy.org/Programming%20Languages/Python/Python%20CheatSheet/beginners_python_cheat_sheet_pcc_testing.pdf) for your reference.