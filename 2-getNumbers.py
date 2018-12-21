# getNumbers(s)
# This function returns all the numbers in a string
# Parameters:
#   s:      str
#           A string with numbers
#
# Return:
#   lst:    list of ints
#           A list with the extracted numbers


def getNumbers(s):
    st = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    lst = []
    tmp = ""
    for x in list(s):
        if x in st:
            tmp += x
        else:
            if tmp != "":
                lst.append(int(tmp))
                tmp = ""
    if tmp is not "":
        lst.append(int(tmp))
    return lst


# Testing with a string with numbers
print(getNumbers('een123zin45 6met-632meerdere+7777getallen12'))

# Testing with a string without numbers
print(getNumbers('een zin zonder meerdere getallen'))

# Testing with a empty string
print(getNumbers(''))
