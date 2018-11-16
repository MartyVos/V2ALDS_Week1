# mymax(a)
# This function returns the maximum value of a list.
# Parameters:
#   a:      list
#           A list of ints or floats
# Return:
#   m:      int
#           The maximum value of the list


def mymax(a):
    assert len(a) != 0
    m = a[0]
    for x in a:
        assert (isinstance(x, int) or isinstance(x, float))
        if x >= m:
            m = x
    return m


# Test with only negative values:
lst = [-2134, -346, -65456, -212, -333, -1]
print(mymax(lst))

# Test with random values
lst = [1, 432, 5, 456, 6745, 56, -45634, 235, 3, 453, 64, 6745]
print(mymax(lst))

# Test with empty list
lst = []
print(mymax(lst))

# Test with string list
lst = ["dhgdsfg", 56, "sdgf"]
print(mymax(lst))
