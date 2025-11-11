import sys

# print("Python version", sys.version)
# print("operating system :",sys.platform)
print(sys.path)
print("enter name:")
name = sys.stdin.readline().rstrip('\n')
print(name)
sys.stdout.write("hola")