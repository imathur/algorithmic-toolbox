# Uses python3
import sys

n = int(sys.argv[1])
prev, curr = 0, 1

for i in range(2,n+1):
    new = curr + prev
    prev = curr
    curr = new

print(new)


