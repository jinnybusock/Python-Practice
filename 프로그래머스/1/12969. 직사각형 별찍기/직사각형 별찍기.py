n, m= map(int, input().split(" "))

for i in range(m):
    for j in range(n):
        if j< n- 1:
            print("*", end= "")
        else:
            print("*")