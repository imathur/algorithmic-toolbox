# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def optimal_sequence(n):
    sequence = []
        
    a = [0]*(n+1)
    
    for each in range(1, len(a)):
        a[each] = a[each-1] + 1
        if each % 2 == 0:
            a[each] = min(1+a[each//2], a[each])
        if each % 3 == 0:
            a[each] = min(1+a[each//3], a[each])
    
    while n > 1:
        sequence.append(n)
        if a[n-1] == a[n]-1:
            n = n - 1
        elif (n % 2 == 0 and a[n//2] == a[n]-1):
            n = n//2     
        elif (n % 3 == 0 and a[n//3] == a[n]-1):
            n = n//3
    
    sequence.append(1)
    
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
