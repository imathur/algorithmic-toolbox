# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)

    starts = zip(starts, [float('-inf')]*len(starts))
    ends = zip(ends, [float('inf')]*len(ends))
    points = zip(points, range(len(points)))

    sorted_list = sorted(chain(starts, ends, points), key=lambda starts: (starts[0], starts[1]))
    stack = []

    for i, j in sorted_list:
        if j == float('-inf'):
            stack.append(j)
        elif j == float('inf'):
            stack.pop()
        else: 
            count[j] = len(stack) 

    return count

def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    count = fast_count_segments(starts, ends, points)
    for x in count:
        print(x, end=' ')
