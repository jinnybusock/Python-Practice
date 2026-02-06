N, M= map(int, input().split())

# 2개의 딕셔너리 사용
numToname= {}
nameTonum= {}

for i in range(1, N+1):
  pokemonName= input()
  numToname[i]= pokemonName
  nameTonum[pokemonName]= i

for i in range(M):
  question= input()

  if question.isdigit():     # 숫자인 경우
    print(numToname[int(question)])
  else:
    print(nameTonum[question])