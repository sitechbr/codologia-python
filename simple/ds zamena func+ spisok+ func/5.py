s = "XXYXXXYXXXXYZZZYZZZZZZ"
k=1
max_sub=0
for i in range(1,len(s)):
    if s[i]==s[i-1] :
        k+=1
        if (k>max_sub):
            max_sub=k
    else:
        k=1

print(max_sub)
