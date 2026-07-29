import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def track_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)
            return result
        return wrapper

    def average_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

optimizer = PerformanceOptimizer()

@optimizer.track_time
def some_heavy_computation(x):
    total = 0
    for i in range(x):
        total += i ** 2
    return total

@optimizer.track_time
def another_heavy_task(y):
    time.sleep(1)
    return y * 2

if __name__ == '__main__':
    some_heavy_computation(10000)
    another_heavy_task(5)
    print('Average execution time:', optimizer.average_time())