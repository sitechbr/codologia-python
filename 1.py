import re

with open("24-153.txt","r") as f:
    s = f.readline()

result = re.findall(r'D.+?[^D]D',s)
res = list(map(len,result))
res.sort()
print(res)

