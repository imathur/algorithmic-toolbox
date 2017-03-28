# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
    
def calc_fib_efficient(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2,n+1):
        new = curr + prev
        prev = curr
        curr = new
    return new

def get_pisano_period(n, m):
    fib_numbers = [0, 1]
    modulos = [0, 1]
    period = 2
    
    for i in range(2, n+1,2):
        print(i)
        
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2]
        modulos[i] = fib_numbers[i] % m
        
        if i < 4:
            continue
        if i % 2 == 0:
            period = i//2
            if arr[:period] == arr[period:]:
                break
    return period

def get_fibonacci_huge_efficient(n, m):
    period = get_pisano_period(n, m)
    n_ = n % period
    fib_small = calc_fib_efficient(n_)
    mod = fib_small % m
    return mod

n, m = int(sys.argv[1]), int(sys.argv[2])
print('remainder = {}'.format(get_fibonacci_huge_efficient(n, m)))

'''
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
'''
