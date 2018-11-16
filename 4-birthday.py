# birthday()
# This function counts the amount of lists that has two equal values.
# Return:
#   c:      int
#           The amount of lists.


def birthday():
    from random import randint
    lst = []
    for i in range(0, 100):
        tmp = []
        for j in range(0, 23):
            tmp.append(randint(1, 365))
        lst.append(tmp)

    c = 0
    for i in lst:
        i1 = i[randint(0, 22)]
        if i.count(i1) == 2:
            c += 1
    return c


print(birthday())
