def sum_diagonals(mx):
    l = len(mx)
    return sum(x[i] + x[l-i-1] for i, x in enumerate(mx)) if l and mx[0] else 0
