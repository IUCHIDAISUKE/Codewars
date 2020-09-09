import collections


def get_strings(city):
    city = city.lower().replace(' ', '')
    lst = []
    for k, v in dict(collections.Counter(city)).items():
        lst.append(k+':'+'*'*v)
    return ','.join(lst)
