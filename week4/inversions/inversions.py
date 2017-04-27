# Uses python3
import sys

def merge(a, b, left, ave, right):
    i, j, k = left, ave, left
    num_inv = 0
    while (i <= ave -1 and j <= right):
        if (a[i] <= a[j]):
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[j]
            num_inv += ave - i
            j += 1
            k += 1
    while (i <= ave - 1):
        b[k] = a[i]
        i += 1
        k += 1
    while (j <= right):
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right+1):
        a[i] = b[i]
    return num_inv
            
def get_number_of_inversions(a, b, left, right):
    num_inv = 0
    if right <= left:
        return num_inv
    ave = (left + right) // 2
    num_inv += get_number_of_inversions(a, b, left, ave)
    num_inv += get_number_of_inversions(a, b, ave+1, right)
    num_inv += merge(a, b, left, ave+1, right)
    return num_inv

# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, raw_input().split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)-1))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))