N, M= map(int, input().split())

wordN= []
wordM= []

for i in range(N):
  wordN.append(input())

for i in range(M):
  wordM.append(input())

count= 0

for word in wordM:
  if word in wordN:
    count+= 1

print(count)