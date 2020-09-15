def halving_sum(n):
    sum = 0
    while n:
        sum += n
        n //= 2
    return sum
