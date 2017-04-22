# Uses python3
import sys

def binary_search(b, x):
    left, right = 0, len(b)
    # write your code here
    mid = left
    while left < right:
        mid = (left+right)//2
        if x == b[mid]:
            return mid
        elif x > b[mid]:
            left = mid+1
        else:
            right = mid
    return mid

def combined_binary_search(a, b, found):
    if len(a) > 0:
        mid_a = (len(a))//2
        mid_b = binary_search(b, a[mid_a])

        b_firsthalf_upper = b_secondhalf_lower = mid_b + 1
        
        if a[mid_a] == b[mid_b]:
            found[mid_b] = mid_a
            b_firsthalf_upper -= 1
            
        
        found[:b_firsthalf_upper] = combined_binary_search(
                                        a[:mid_a],
                                        b[:b_firsthalf_upper], 
                                        found[:b_firsthalf_upper]
                                    )
        found[b_secondhalf_lower:] = combined_binary_search(
                                         a[mid_a:],
                                         b[b_secondhalf_lower:],
                                         found[b_secondhalf_lower:]
                                     )
        return found


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    b = sorted(data[n + 2:])
    found = [-1 for _ in range(len(b))]
    # for x in b:
    #     # replace with the call to binary_search when implemented
    #     print(binary_search(a, x), end = ' ')

    found = combined_binary_search(a, b, found)
    print(' '.join([str(each) for each in found]))
