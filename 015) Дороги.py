n = int(input())
count = 0

for i in range(n):
    numbers = list(map(int, input().split()))

    for k in range(i + 1, n):
        count += numbers[k]

print(count)