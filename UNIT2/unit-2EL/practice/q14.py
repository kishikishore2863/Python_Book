try:
    li= ["follow banger\n","big bang theory\n"]
    with open('demo.txt','a+')as f:
        f.writelines(li)

except Exception as e:
    print(e)