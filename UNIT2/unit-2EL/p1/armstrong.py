def isArm(n):
    dummy ,n1 =n,n

    count = 0
    lengthofn =0
    while n>0:
        lengthofn +=1
        n=n//10
    while n1>0:
        last = n1%10
        count +=last**lengthofn
        n1=n1//10
    return dummy ==count


print(isArm(153))