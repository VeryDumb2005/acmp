k, n = map(int, input().split())
ladder_list = [0] * (n + 1)
ladder_list[0] = 1

for i in range(1, n + 1):
    start = max(0, i - k)
    ladder_list[i] = sum(ladder_list[start:i])

print(ladder_list[n])