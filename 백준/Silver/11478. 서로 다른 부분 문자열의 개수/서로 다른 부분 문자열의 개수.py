word= input()
partial= set()

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        temp= word[i:j]
        partial.add(temp)

print(len(partial))