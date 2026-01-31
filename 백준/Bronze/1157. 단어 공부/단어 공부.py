from collections import Counter

word = input().upper()

word_count = Counter(word)

most = word_count.most_common(2)

if len(most) == 1:
    print(most[0][0])
elif most[0][1] == most[1][1]:
    print("?")
else:
    print(most[0][0])