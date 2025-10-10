
# 6

def lps(pattern):
    m=len(pattern)
    lps=[0]*m
    length=0
    i=1
    while i<m:
        if pattern[i]==pattern[length]:
            length=length+1
            lps[i]=length
            i=i+1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i=i+1
        
    return lps

def kmp(text,pattern):
    n=len(text)
    m=len(pattern)
    l_p_s=lps(pattern)
    j=0
    i=0
    results=[]
    while i<n:
        if pattern[j]==text[i]:
            i+=1
            j+=1
        if j==m:
            results.append(i-j)
            j=l_p_s[j-1]
        elif(i<n and text[i]!=pattern[j]):
            if j!=0:
                j=l_p_s[j-1]
            else:
                i+=1
            
    return results
text = "CATSABCBCABCDOGSABCBCABC"
pattern = "ABCBCABC"

matches = kmp(text, pattern)
print("Pattern found at indices:", matches)


