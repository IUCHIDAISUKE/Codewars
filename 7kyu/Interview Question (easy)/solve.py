def get_strings(city):
    city = city.lower()
    city = "".join(city.split())
    dic = {}
    for i in city:
        dic[i] = dic.get(i, 0)+1
    print(dic)
    s = ""
    for k, v in dic.items():
        s += k+":"
        for _ in range(v):
            s += "*"
        s += ","
    return s[:-1]
