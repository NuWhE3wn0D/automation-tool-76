import time

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return time.time() - self.start_time

    def log_performance(self, process_name):
        elapsed = self.elapsed_time()
        print(f'Performance of {process_name}: {elapsed:.4f} seconds')
        self.start_time = time.time()

monitor = PerformanceMonitor()

# Example usage in a function

def heavy_computation():
    # Simulating heavy computation
    time.sleep(2)  
    monitor.log_performance('heavy_computation')

if __name__ == '__main__':
    heavy_computation()