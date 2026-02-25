firstSon, firstMot= map(int, input().split())
secondSon, secondMot= map(int, input().split())

def gcd(a, b):
  while b:
    a, b= b, a%b
  
  return a

commonMot= firstMot* secondMot // gcd(firstMot, secondMot)
afterFirstSon= firstSon*commonMot//firstMot
afterSecondSon= secondSon* commonMot// secondMot

after= afterFirstSon+ afterSecondSon
num= gcd(after, commonMot)

print(f"{after// num} {commonMot// num}")