T= int(input())

def gcd(a, b):
    while b:
        a, b= b, a% b
        
    return a

for i in range(T):
    a, b= map(int, input().split())
    
    divide= gcd(a, b)
    
    print(a*b // divide)
    