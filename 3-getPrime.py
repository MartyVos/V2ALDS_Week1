# generateList()
# This function generates a list of values in a specified range and returns the generated list.
# Parameters:
#   begin:  int
#           The starting value of the list.
#   end:    int
#           The last value
#
# Return:
#   lst:    list of ints
#           The generated list ranging from begin to end.


def generateList(begin, end):
    lst = []
    for x in range(begin, end+1):
        lst.append(x)
    return lst


# getPrime(begin=2, end=1000)
# This function prints all prime numbers from a list of values in a specified range.
# Parameters:
#   max:    int
#           The maximum value to search for prime numbers. Default value of 1000.


def getPrime(max=1000):
    assert max > 2
    primeLst = generateList(2, max)
    tmpLst = []
    index = 0
    for i in primeLst:
        for j in range(i+index, len(primeLst), i):
            tmpLst.append(primeLst[j])
        index += 1

    for k in tmpLst:
        if k in primeLst:
            primeLst.pop(primeLst.index(k))

    print(primeLst)

# Testing for default value (1000).
getPrime()

# Testing for small number.
getPrime(25)

# Testing for value of 0.
getPrime(0)
