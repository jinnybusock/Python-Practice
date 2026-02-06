N= int(input())
exist= set(map(int, input().split()))

M= int(input())
given= list(map(int, input().split()))

result= []

for num in given:
  if num in exist:
    result.append(1)
  else:
    result.append(0)

print(*result)