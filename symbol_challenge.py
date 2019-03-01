def SimpleSymbols(str):
    symbol = '+'

    for i in range(0, len(str)):
        if str[i].isalpha():
            if str[i - 1] != symbol or str[i + 1] != symbol:
                print("bullshit")

    return (print('haan'))


# keep this function call here
print(SimpleSymbols(input()))
