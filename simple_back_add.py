def SimpleAdding(num):
    result = 0
    num = int(num)
    for i in range(1, num + 1):
        if num == 0:
            result = 0
        else:
            result = result + i
    return result


# keep this function call here
print(SimpleAdding(input()))
