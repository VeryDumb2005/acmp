a, b, c, d = map(int, input().split())
answer = set()

for x in range(-100, 101):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        answer.add(x)

print(*sorted(answer))