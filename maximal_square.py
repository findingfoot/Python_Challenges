def MaximalSquare(strArr):
    squarevalue = []
    base_value = 1
    for s in strArr:
        row = []
        for i in s:
            if i == '0':
                row.append(0)
            else:
                row.append(1)
        squarevalue.append(row)

    for p in range(1, len(squarevalue)):
        for q in range(1, len(squarevalue[p])):
            if squarevalue[p][q] > 0:
                squarevalue[p][q] = 1 + min(squarevalue[p - 1][q], squarevalue[p][q - 1], squarevalue[p - 1][q - 1])
                if squarevalue[p][q] > base_value:
                    base_value = squarevalue[p][q]

    return base_value * base_value



print (MaximalSquare(input()))