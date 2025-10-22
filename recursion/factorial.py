
def fact(number):
    if number == 1:
        return 1

    return number*fact(number-1)


res = fact(5)
print(res)