def points(games):
    return sum([3 if i[0] > i[2] else 1 if i[0] == i[2] else 0 for i in games])
