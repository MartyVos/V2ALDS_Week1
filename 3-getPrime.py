# getPrime(begin=2, end=1000)
# This function prints all prime numbers from a list of values in a specified range.
# Parameters:
#   max:    int
#           The maximum value to search for prime numbers. Default value of 1000.


def getPrime(max=1000):
    assert max > 2
    tmp = [True] * (max + 1)

    for k in range(2, max):
        waarde = 2 * k
        while waarde < max:

            tmp[waarde] = False
            waarde += k

    primeList = []
    for i in range(2, max):
        if tmp[i]:
            primeList.append(i)

    return primeList


# Testing for default value (1000).
print(getPrime())

# Testing for small number.
# getPrime(25)

# Testing for value of 0.
# getPrime(0)
