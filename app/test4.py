import time

# let's imagine your app needs to make an expensive api call
def compute(x):
    response = expensive_api_call()
    return response + x


def expensive_api_call():
    time.sleep(1000) # takes 1,000 seconds
    return 123