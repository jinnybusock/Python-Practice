N= int(input())
count= 0

for i in range(N):
    word= input()
    seen= set()
    prev= ""
    is_group= True

    for k in range(len(word)):
        if k== 0:
            prev= word[0]

        elif k> 0:
            if word[k] != word[k-1]:
                seen.add(word[k-1])
                prev= word[k]

            if word[k] in seen:
                is_group= False
                break

    if is_group:
        count += 1

print(count)