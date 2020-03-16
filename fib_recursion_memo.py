import time

memo = { 0: 0, 1: 1 }

def fib(n):
    if n not in memo:
        memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]

# Check result

if __name__ == '__main__':

    start_time = time.time()

    print(fib(30))

    print("--- {} seconds ---".format(time.time() - start_time))
