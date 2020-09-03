def base_finder(seq):
    li = [int(x) for x in seq]
    li.sort()
    tmp = li[0]
    for num in li[1:]:
        if num % 10 == 0:
            return tmp % 10+1
        tmp = num
    return len(li)
