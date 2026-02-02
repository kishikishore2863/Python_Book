if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        q = input()
        str_arr = q.split(" ")
        if str_arr[0] == 'insert':
            l.insert(int(str_arr[1]), int(str_arr[2]))
        if str_arr[0] == 'print':
            print(l)
        if str_arr[0] == 'remove':
            l.remove(int(str_arr[1]))
        if str_arr[0] == 'append':
            l.append(int(str_arr[1]))
        if str_arr[0] == 'pop':
            l.pop()
        if str_arr[0] == 'reverse':
            l.reverse()

