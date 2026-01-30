others= set()

for i in range(10):
    num= int(input())
    others.add(num%42)
   
print(len(others))