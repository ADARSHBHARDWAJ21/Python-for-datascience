import time

def timer_eval(func): 
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time} seconds to execute.')
        return result
    return wrapper
@timer_eval
def demo_func(n):
    time.sleep(n)

# function calling
demo_func(3)


