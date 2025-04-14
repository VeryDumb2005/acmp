n = int(input())
days_list = map(int, input().split())
odd_days = []
even_days = []

for day in days_list:
    if day % 2 == 0:
        even_days.append(day)
    else:
        odd_days.append(day)

print(*odd_days)
print(*even_days)
if len(even_days) >= len(odd_days):
    print("YES")
else:
    print("NO")