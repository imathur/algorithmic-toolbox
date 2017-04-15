# Uses python3
import sys

def get_change(m):
    #write your code here
    total = 0
    if m < 5:
    	total = m
    elif m < 10:
    	total = 1 + (m % 5)
    else:
    	total = m//10
    	m = m % 10
    	total += m//5 + m%5

    return total

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(sys.argv[1])
    print(get_change(m))
