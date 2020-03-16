import time
from functools import lru_cache

@lru_cache(maxsize = None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

# Check result

if __name__ == '__main__':
  
    start_time = time.time()

    print(fib(30))

    print("--- {} seconds ---".format(time.time() - start_time))
