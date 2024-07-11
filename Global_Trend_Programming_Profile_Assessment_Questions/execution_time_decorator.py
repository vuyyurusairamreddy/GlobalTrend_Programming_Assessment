# Filename: execution_time_decorator.py

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time
def expensive_task():
    time.sleep(2)
    return "Task completed"

# Usage Example
print(expensive_task())  # Output: Task completed
                         # Execution time: 2.0... seconds
