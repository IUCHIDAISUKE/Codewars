def longest(s1, s2):
    dic = {}
    s1 = s1+s2
    for i in s1:
        dic[i] = dic.get(i, 1) + 1
    dic = sorted(dic.items(), key=lambda i: i[0])
    return "".join(k for k, v in dic)
