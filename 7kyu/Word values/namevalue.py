def name_value(my_list):
    li = []
    for num, i in enumerate(my_list):
        cnt = 0
        i = i.replace(' ', '')
        for j in list(i):
            cnt += int(ord(j) - ord('a')+1)
        li.append(cnt * (num + 1))
    return li
