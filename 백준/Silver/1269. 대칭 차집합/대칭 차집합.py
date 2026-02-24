A, B= map(int, input().split())

A_nums= set(map(int, input().split()))
B_nums= set(map(int, input().split()))

common= []

for num in A_nums:
  if num in B_nums:
    common.append(num)

for num in common:
  A_nums.discard(num)
  B_nums.discard(num)

print(len(A_nums)+ len(B_nums))