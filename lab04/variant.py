n = int(input())

count = 0
total = 0

for _ in range(n):
    x = int(input())

    if 10 <= x <= 20:
        count += 1
        total += x

print(count)
print(total)
