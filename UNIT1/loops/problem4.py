#given number is prime or not

number = int(input("enter the number "))


def fun(number):
    for i in range(2,number):
        if(number%i == 0):
            return 0
            break
    return 1


res = fun(number)
if res == 0:
    print("NOT PRIME")
else:
    print("PRIME")


