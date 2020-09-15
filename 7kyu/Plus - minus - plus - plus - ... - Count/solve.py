def catch_sign_change(lst):
    cnt = 0
    for i, j in zip(lst[1:], lst):
        if (i < 0 and 0 <= j) or (i >= 0 and j < 0):
            cnt += 1
    return cnt
