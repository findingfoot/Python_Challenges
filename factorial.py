def FirstFactorial(num):
    fact = 1
    num = int(num)

    if (num < 0):
        print("factorial doesnt exist")
    elif num == 0:
        print("Factorial is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i

    return fact


# keep this function call here
print(FirstFactorial(input()))
