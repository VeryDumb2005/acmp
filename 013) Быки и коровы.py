a, b = input().split()
bulls = 0
cows = 0

for i in range(4):
    if a[i] == b[i]:
        bulls += 1
    elif b[i] in a:
        cows += 1

print(bulls, cows)