

# To print the matrix with input i and j

# use if and else to make it better
m=[[0,0],[0,0],[0,0]]
m[0][0]=1
m[0][1]=2
m[1][0]=3
m[1][1]=4
m[2][0]=5
m[2][1]=6
i=int(input("Enter the ith row: "))-1
j=int(input("Enter the jth column: "))-1
for r in m:
    print(r)
print(f"The number is: {m[i][j]}")

