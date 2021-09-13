import os
f = os.listdir("F:\pythonProject")
def root(not_digit):
    file = open(not_digit, 'r')
    line = file.readlines()
    Sum = 0
    for digit in line:
        if digit.strip().isdigit() == True:
            Sum = Sum + int(digit)
        else:
            A = root(digit.strip())
            Sum = Sum + A
    return Sum
for x in f:
    Sum = 0
    if 'txt' == x.split(".")[-1]:
        file = open( x, 'r')
        line = file.readlines()
        sum = 0
        for digit in line:
            if digit.strip().isdigit() == True:
                Sum = Sum + int(digit)
            else:
                A = root(digit.strip())
                Sum = Sum + A
        print(x, "Total:", Sum)







