def spacey(array):
    li = [array[0]]
    for i in array[1:]:
        li.append(li[-1]+i)
    return li
