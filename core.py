import time

class Performance:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        return time.time() - self.start_time

    def timeit(self, func):
        def wrapper(*args, **kwargs):
            self.start()
            result = func(*args, **kwargs)
            elapsed = self.stop()
            print(f'Function {func.__name__} took {elapsed:.4f} seconds.')
            return result
        return wrapper

@Performance().timeit
def expensive_operation(data):
    total = 0
    for number in data:
        total += number ** 2
    return total

if __name__ == '__main__':
    data = range(10000)
    result = expensive_operation(data)
    print(f'Result: {result}')