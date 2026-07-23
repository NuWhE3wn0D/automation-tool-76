import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def log_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            self.execution_times.append((func.__name__, end_time - start_time))
            return result
        return wrapper

    def get_average_time(self):
        if not self.execution_times:
            return 0
        total_time = sum(time for _, time in self.execution_times)
        return total_time / len(self.execution_times)

optimizer = PerformanceOptimizer()

@optimizer.log_time
def sample_function(x):
    time.sleep(x)
    return x

if __name__ == '__main__':
    for i in range(1, 5):
        sample_function(i)
    print(f'Average Execution Time: {optimizer.get_average_time()} seconds')