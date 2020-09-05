def even_chars(st):
    if len(st) < 2 or 100 < len(st):
        return "invalid string"
    return list(st[1::2])


print(even_chars("a"))
