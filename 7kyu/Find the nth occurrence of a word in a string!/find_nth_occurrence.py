def find_nth_occurrence(substring, string, occurrence=1):
    se = set()
    for i in range(len(string)):
        se.add(string.find(substring, i))
    li = sorted(list(se))
    return li[occurrence] if occurrence < len(li) else -1
