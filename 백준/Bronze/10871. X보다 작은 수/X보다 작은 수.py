N, num= map(int, input().split())

nums= list(map(int, input().split()))
output= []

for i in range(N):
    if nums[i] < num:
        output.append(nums[i])

print(*output)