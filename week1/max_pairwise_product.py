# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

highest = a.pop(a.index(max(a)))
secondhighest = max(a)

result = highest*secondhighest
print(result)
