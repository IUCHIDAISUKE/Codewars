def nb_dig(n, d):
    lst = list(map(lambda x: x**2, range(n+1)))
    return sum([str(i).count(str(d)) for i in lst])
