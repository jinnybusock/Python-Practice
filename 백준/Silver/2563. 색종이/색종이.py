N= int(input())
grid= [[0]* 100 for i in range(100)]

for i in range(N):
    x, y= map(int, input().split())
    for ga in range(x, x+10):
        for se in range(y, y+10):
            grid[ga][se]= 1

total= 0

for i in range(100):
    for k in range(100):
        if grid[i][k] == 1:
            total+= 1
            
print(total)