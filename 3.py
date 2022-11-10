import re

with open("k7a-1.txt","r") as f:
    s = f.readline()

result = re.findall(r'[ABC]*',s)
res = list(map(len,result))
print(max(res))

