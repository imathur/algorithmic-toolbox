# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def calc_fib_efficient(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2,n+1):
        new = curr + prev
        prev = curr
        curr = new
    return new

def get_pisano_period(m):
    modulos = [0, 1]
    while True:
        modulos.append((modulos[-1] + modulos[-2]) % m)
        if modulos[-1] == 1 and modulos[-2] == 0:
            return len(modulos) - 2

def get_fibonacci_huge_efficient(n, m):
    period = get_pisano_period(m)
    if period:
        n_ = n % period
    else:
        n_ = n
    fib_small = calc_fib_efficient(n_)
    mod = fib_small % m
    
    return mod

def fibonacci_partial_sum_efficient(m, n):
    mod_n = get_fibonacci_huge_efficient(n+2, 10)
    mod_m_minus_1 = get_fibonacci_huge_efficient(m+1, 10)
    return ((mod_n % 10) - (mod_m_minus_1 % 10)) % 10
    

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_efficient(from_, to))
