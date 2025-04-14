import re


move = input()

if re.fullmatch(r'^[A-H][1-8]-[A-H][1-8]$', move):
    x1, y1, x2, y2 = move[0], move[1], move[3], move[4]

    x1 = ord(x1) - ord('A') + 1
    y1 = int(y1)

    x2 = ord(x2) - ord('A') + 1
    y2 = int(y2)

    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2)

    if x_diff * y_diff == 2:
        print('YES')
    else:
        print('NO')
else:
    print('ERROR')