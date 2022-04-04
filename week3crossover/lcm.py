def findlcm(a, b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            break
        maximum = maximum + 1
    return maximum


def menu():
    a = int(input(" Enter the First Value for LCM: "))
    b = int(input(" Enter the Second Value for LCM: "))
    lcm = findlcm(a, b)
    print("\n Least Common Multiple of {0} and {1} is: {2}".format(a, b, lcm))
    print()