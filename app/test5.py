import time

"""
Let's imagine your app needs to make an expensive api call
Implement a simple mock function of compute in
its corresponding unit test case (./test/test_test5.py)
to bypass the operation and pass the test.
"""


def compute(x):
    response = expensive_api_call()
    return response + x


def expensive_api_call():
    time.sleep(1000)  # takes 1,000 seconds
    return 123
