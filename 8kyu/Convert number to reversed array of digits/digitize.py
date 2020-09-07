def digitize(n):
    return [int(i) for i in str(n)[::-1]]


print(digitize(8635647))
