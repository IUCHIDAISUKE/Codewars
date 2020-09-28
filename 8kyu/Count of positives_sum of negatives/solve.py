def count_positives_sum_negatives(arr):
    aa = 0
    bb = 0
    for i in arr:
        if i > 0:
            aa += 1
        else:
            bb += i
    return [aa, bb] if arr else []
