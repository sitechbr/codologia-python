print("ВВедите координату x коня")
x1=int(input())
print("ВВедите координату y коня")
y1=int(input())
print("ВВедите координату x коня")
x2=int(input())
print("ВВедите координату y коня")
y2 = int(input())


if ((x1+2)==x2 and ((y1+1) == y2 or (y1-1) == y2)) or ((x1-2)==x2 and ((y1+1) == y2 or (y1-1) == y2)) or ((y1+2)==y2 and ((x1+1) == x2 or (x1-1) == x2)) or ((y1+2)==y2 and ((x1+1) == x2 or (x1-1) == x2)) or ((y1-2)==y2 and ((x1+1) == x2 or (x1-1) == x2)):
    print("YES")
else:
    print("NO")

