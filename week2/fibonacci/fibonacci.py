# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_efficient(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2,n+1):
        new = curr + prev
        prev = curr
        curr = new
    return new

n = int(input())
print(calc_fib_efficient(n))
