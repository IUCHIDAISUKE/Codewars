def check_exam(arr1, arr2):
    ans = 0
    for a, b in zip(arr1, arr2):
        if a == b:
            ans += 4
        elif b == '':
            continue
        else:
            ans -= 1
    return ans if ans > 0 else 0
