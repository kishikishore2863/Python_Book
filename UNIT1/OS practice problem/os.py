# current_dir = os.getcwd()
# print(current_dir)
# new_dir = "new_dir"
# os.mkdir(new_dir)
# print(os.listdir())
# updated_dir = os.chdir(new_dir)
print(os.getcwd())
if os.path.exists("kis"):
    os.rmdir("kis")
else:
    print("dir not present")

path = os.getcwd()
filename= "os.py"
filepath =  os.path.join(path, filename)
print(filepath)

print(os.path.isfile(filepath))

# env = os.environ
# for key,value in env.items():
#     print(f"{key}:{value}")

pipe = os.popen(filepath)
print(pipe.read())



