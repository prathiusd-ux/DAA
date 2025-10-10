
# 2. to calculate the number of times The occured in a string text
txt=input("Enter a string: ")
i=0
found=1
x="the"
for x in range (len(txt)):
    if txt[i].lower()==x:
        found+1
    

print(i)
print(f"The number of times the occured in the string is: {found} ")
