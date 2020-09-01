def points(a):
    for x, y in (s.split(":") for s in a):
        print(type(x), y)
# return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))


print(points(['1:0', '2:0', '3:0', '4:0', '2:1',
              '3:1', '4:1', '3:2', '4:2', '4:3']))
