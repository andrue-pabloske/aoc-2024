data = open('01.txt', 'r').read().split('\n')
n = len(data)

a = [0] * n
b = [0] * n
for i in range(n):
    line = data[i].split('   ')
    a[i] = int(line[0])
    b[i] = int(line[1])

# Part 1
'''
a.sort()
b.sort()
ans = 0
for i in range(n):
    ans += abs(a[i] - b[i])
print(ans)
'''

# Part 2
from collections import defaultdict
count = defaultdict(int)
for num in b:
    count[num] += 1

ans = 0
for num in a:
    ans += num * count[num]
print(ans)