import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

# Sample Input
num = 25100
delay = 2123
delayed_sqrt(num, delay)
