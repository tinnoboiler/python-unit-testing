import time

"""
Let's imagine your app needs to make an expensive api call
Implement a smarter version of mock function using side_effect in
its corresponding unit test case (./test/test_test6.py)
that can __simulate__ the actual operation and pass the test.
"""


# let's imagine your app needs to make an expensive api call
def compute(x):
    response = expensive_smart_api_call(x)
    return response


def expensive_smart_api_call(x):
    time.sleep(1000)  # takes 1,000 seconds
    return x * 2  # imagine that it did some processing on the input
