
# 5. Implementing LPS table;
pattern="ABCBCABC"
n=len(pattern)
lps=[0]*n
length=0
i=1
while i<n:
    if pattern[i]==pattern[length]:
        length=length+1
        lps[i]=length
        i=i+1
    else:
        if length!=0:
            length=lps[length]
        else:
            lps[i]=0
            i=i+1
    
print(lps)