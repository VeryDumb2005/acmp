n = int(input())
count = 0

for _ in range(n):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    cross1 = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    cross2 = (x3 - x2) * (y - y2) - (y3 - y2) * (x - x2)
    cross3 = (x4 - x3) * (y - y3) - (y4 - y3) * (x - x3)
    cross4 = (x1 - x4) * (y - y4) - (y1 - y4) * (x - x4)

    if (cross1 <= 0 and cross2 <= 0 and cross3 <= 0 and cross4 <= 0 or
            cross1 >= 0 and cross2 >= 0 and cross3 >= 0 and cross4 >= 0):
        count += 1

print(count)