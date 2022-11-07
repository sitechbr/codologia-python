n = int(input())
l = []
k=0

print("Введите количество чисел")
print("Введите сами числа")
for i in range(n):
    print("Введите", i, "число")
    l.append(int(input()))


for i in range(n):
    if (l[i]%5 == 0):
        k+=1
print("Количество чисел кратных 5:",k)