# with open('data.txt','r')as file:
#     for line in file:
#         line = line.strip()
#         try:
#             number = int(line)
#             print("Converted",number)
#         except ValueError:
#             print("Skipping invalid integer:",line)
#             continue
#
# with open('data.txt','r')as file:
#     lines =[]
#     for _ in range(5):
#         line = file.readline()
#         if line == "":
#             break
#         lines.append(line.rstrip())
#
#     print(lines)
from re import search

#
# s ="1"
# try:
#     n = int(s)
# except ValueError:
#     print("v")

# try:
#     with open('data.txt','r')as f:
#         names = [line.strip() for line in f ]
#         print(names)
#         search = input("enter search")
#         if search in names:
#             print("e ")
#         else:
#             print("no")
# except FileNotFoundError:
#     print("errrr")
#
# count =0
# sum =0
# with open('data.txt','r')as f:
#     for i in f:
#         try:
#             mark = int(i.strip())
#             count += 1
#             sum = sum +mark
#         except ValueError:
#             continue
# if count == 0:
#     print("no")
# else:
#     print(sum)
#     print(sum/count)








