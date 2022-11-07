import random

l=[]
print("Inpunt count numbers")
n=int(input())

for i in range(n):
   l.append(random.randint(0,100))
print(l)

l.sort()
print(l)