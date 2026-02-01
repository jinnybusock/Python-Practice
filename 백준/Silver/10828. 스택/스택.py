N= int(input())
temp= list()

for i in range(N):
    word= input().split()

    if word[0]== "push":
        num= int(word[1])
        temp.append(num)

    elif word[0]== "pop":
        if len(temp) != 0:
            print(temp.pop())
        else:
            print(-1)

    elif word[0]== "size":
        print(len(temp))

    elif word[0] == "empty":
        if len(temp)== 0:
            print(1)
        else:
            print("0")

    else:
        if len(temp) != 0:
            print(temp[-1])
        else:
            print(-1)