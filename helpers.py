def memoize(func):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def batch_process(items, function, batch_size=10):
    for i in range(0, len(items), batch_size):
        yield function(items[i:i + batch_size])

def parallel_process(func, iterable):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        return list(executor.map(func, iterable))

if __name__ == '__main__':
    print(fibonacci(10))
    print(list(batch_process(range(100), sum)))
    print(parallel_process(lambda x: x * 2, range(10)))