from itertools import accumulate

# def spacey(a):
#     return list(accumulate(a))


def spacey(array):
    return [''.join(array[:i+1]) for i in range(len(array))]
