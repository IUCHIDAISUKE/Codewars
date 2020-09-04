def word_pattern(word):
    li, dic, cnt = [], {}, 0
    for i in word.lower():
        if i not in dic:
            dic[i] = str(cnt)
            cnt += 1
        li.append(dic[i])
    return '.'.join(li)
