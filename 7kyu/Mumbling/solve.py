def accum(s):
    lst = []
    for num, v in enumerate(s):
        lst.append(v.upper()+v.lower()*num)
    return '-'.join(lst)
