def descending_order(num):
    li = sorted(list(str(num)), reverse=True)
    num = 0
    for i in li:
        num = num*10+int(i)
    return num
