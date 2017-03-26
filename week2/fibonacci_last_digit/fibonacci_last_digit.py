# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
    
def get_fibonacci_last_digit(n):
    prev, curr = 0, 1

    for i in range(2,n+1):
        new = (curr + prev) % 10
        prev = curr
        curr = new
    
    return new

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(get_fibonacci_last_digit(n))
