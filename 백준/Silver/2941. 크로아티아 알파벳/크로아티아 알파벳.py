word= input()
count= 0
i= 0

specials= ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

while i< len(word) :
    matched= False
    for s in specials:
        if word[i: i+len(s)] == s:
            count+= 1
            i+= len(s)
            matched= True
            break

    if not matched:
        count+= 1
        i += 1

print(count)