def amicable(a, b):
    sum_a = 0
    sum_b = 0
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            sum_a += i
            if (i != 1):
                sum_a += int(a/i)

    for i in range(1, int(b ** 0.5) + 1):
        if b % i == 0:
            sum_b += i
            # To Exclude B itself
            if (i != 1):
                sum_b += int(b/i)

    if(sum_a == b and sum_b == a):
        return True
    else:
        return False

print(amicable(284, 220))