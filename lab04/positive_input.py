rejected = 0

while True:
    x = int(input())

    if x > 0:
        break

    rejected += 1

print(x * x)
print(rejected)