def cost(mins):
    print(mins)
    ck = mins // 15
    ans = 0
    if mins < 65:
        ans += 30
    else:
        ans += 30
        mins -= 65
        ans += (mins+29) // 30 * 10
    return ans
