def all_non_consecutive(arr):
    li = []
    tmp = arr[0]
    for num, v in enumerate(arr[1:]):
        if tmp + 1 != v:
            dic = {}
            dic['i'] = num + 1
            dic['n'] = v
            li.append(dic)
        tmp = v
    return li
