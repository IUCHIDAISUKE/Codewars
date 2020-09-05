def no_boring_zeros(n):
    return 0 if n == 0 else n if n % 10 != 0 else no_boring_zeros(n//10)
