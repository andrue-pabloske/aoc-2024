data = open('02.txt', 'r').read().split('\n')
n = len(data)

# Part 1
'''
ans = 0
for line in data:
    report = [int(level) for level in line.split(' ')]
    increasing = report[1] > report[0]
    safe = True
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) > 3 or abs(report[i] - report[i - 1]) < 1 or ((report[i] > report[i - 1]) ^ increasing):
            safe = False
            break
    if safe:
        ans += 1

print(ans)
'''

# Part 2
ans = 0
for line in data:
    report = [int(level) for level in line.split(' ')]
    increasing = report[1] > report[0]
    safe = True
    level_removed = False
    i = 1
    while i < len(report):
        if abs(report[i] - report[i - 1]) > 3 or abs(report[i] - report[i - 1]) < 1 or ((report[i] > report[i - 1]) ^ increasing):
            if level_removed:
                safe = False
                break
            level_removed = True
            report.pop(i)
            i -= 1
        i += 1
    if safe:
        ans += 1

print(ans)