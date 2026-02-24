N, M= map(int, input().split())

first_seen= set()
first_hear= set()

for i in range(N):
  first_seen.add(input())

for i in range(M):
  first_hear.add(input())

count= 0
first_time= []

for name in first_seen:
  if name in first_hear:
    count += 1
    first_time.append(name)

first_time.sort()

print(count)
for i in range(count):
  print(first_time[i])