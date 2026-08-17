def fib(k):
    if k <= 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

def print_fibonacci(n, i=0):
    if n <= 0:
        print("No terms to display")
        return
    if i == n:
        print()
        return
    print(fib(i), end=" ")
    print_fibonacci(n, i + 1)
print(print_fibonacci(7))
print(print_fibonacci(2))
print(print_fibonacci(-5))
