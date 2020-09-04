def word_pattern(word):
    cnt = 1
    dic = {word[0].lower(): 0}
    li = [0]
    for i in word[1:]:
        i = i.lower()
        if i in dic:
            li.append(dic[i])
        else:
            dic[i] = cnt
            cnt += 1
            li.append(dic[i])
    return '.'.join([str(i) for i in li])
