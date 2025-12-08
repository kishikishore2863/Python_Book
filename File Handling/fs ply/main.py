f = open('demo.txt','r+')

for i in range(3):
    print(f.readline(),end="")


f.write(" hello from c")

f.close()