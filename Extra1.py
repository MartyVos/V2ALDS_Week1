# next_las_seq(lst)
# This function returns the next look-and-say sequence.
# Parameters:
#   lst:    list of ints
#           The first sequence
# Return:
#   nxt:    List of ints
#           The next sequence


def next_las_seq(lst):
    nxt = []
    tmp = 1
    for i in range(len(lst)):
        if i == len(lst) - 1:
            nxt.append(tmp)
            nxt.append(lst[i])
        elif lst[i] == lst[i+1]:
            tmp += 1
        else:
            nxt.append(tmp)
            nxt.append(lst[i])
            tmp = 1

    return nxt


# Starting with one value
x = [1]
a = 0
while a < 10:
    x = next_las_seq(x)
    print(x)
    a += 1
print("-")

# Testing with example list:    [3,3,4,1,1,6,6,6,1]
# Expected output:              [2,3,1,4,2,1,3,6,1,1]
x = [3, 3, 4, 1, 1, 6, 6, 6, 1]
print(next_las_seq(x))
