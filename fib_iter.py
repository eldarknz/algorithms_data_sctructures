import time

def fib(n):
    if n == 0:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

# Check result

if __name__ == "__main__":

    start_time = time.time()

    print(fib(30))

    print("--- {} seconds ---".format(time.time() - start_time)) 
