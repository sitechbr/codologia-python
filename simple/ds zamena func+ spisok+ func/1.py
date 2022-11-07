print("Введите количество чисел")
n = int(input())
l = []
for i in range(n):
    print("Введите", i, "число")
    l.append(int(input()))
print(l)

print("===========================")
for i in range(n):
    print(i, "число в списке равно", l[i])
print("===========================")
for i in range(n):
    if (l[i]%5 == 0):
        print(l[i], "делится на 5")
