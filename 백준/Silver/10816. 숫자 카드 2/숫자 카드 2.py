N= int(input())

cards= list(map(int, input().split()))

M= int(input())

nums= list(map(int, input().split()))

count= {}

for card in cards:
    if card in count:
        count[card] += 1
        
    else:
        count[card]= 1
        
result= []

for num in nums:
    if num in count:
        result.append(count[num])
        
    else:
        result.append(0)
        
print(*result)