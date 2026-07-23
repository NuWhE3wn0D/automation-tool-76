import time

class PerformanceOptimizer:
    def __init__(self, threshold=1.0):
        self.threshold = threshold

    def time_execution(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > self.threshold:
                print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
            return result
        return wrapper

@PerformanceOptimizer(threshold=0.5).time_execution
def heavy_computation(n):
    total = 0
    for i in range(n):
        total += sum(j ** 2 for j in range(10000))
    return total

@PerformanceOptimizer().time_execution
def quick_function():
    return sum(range(100))
