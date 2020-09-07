def pluck(objs, name):
    return [dic.get(name, None) for dic in objs]
