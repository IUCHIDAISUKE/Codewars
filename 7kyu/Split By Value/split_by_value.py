def split_by_value(k, elements):
    lmi = [i for i in elements if i < k]
    lma = [i for i in elements if k <= i]
    return lmi + lma
