import time

# T(n) = 1 + n = O(n)
def sum_of_n_iter(n):
    start_time = time.time()
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    end_time = time.time()
    return sum, end_time - start_time

# T(n) = 1 = O(1)
def sum_of_n_formula(n):
    start_time = time.time()
    sum = (n * (n + 1)) // 2
    end_time = time.time()
    return sum, end_time - start_time

for i in range(5):
    n = 1000000
    # Run time increases linearly with increase in n
    sum, duration = sum_of_n_iter(n)
    print(f"Sum of {n} integers using iterative procedure is {sum} and it took {duration} to execute")

for i in range(5):
    n = 1000000
    # Run time is constant
    sum, duration = sum_of_n_formula(n)
    print(f"Sum of {n} integers using equation is {sum} and it took {duration} to execute")    