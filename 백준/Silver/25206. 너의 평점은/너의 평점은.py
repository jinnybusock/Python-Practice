score_manual= {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

middle= 0.0
total= 0

for _ in range(20):
    subject, importance, score = input().split()
    importance= float(importance)

    if score== 'P':
        continue
    else:
        middle+= importance * score_manual.get(score)
        total+= importance

print(middle/total)