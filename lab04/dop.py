n = int(input())

if n < 2:
    print("NO")
else:
    divisor = 2
    is_prime = True

    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print("YES")
    else:
        print("NO")