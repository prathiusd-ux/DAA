print("Enter number: ")
num = input()
print("You entered: " + num)
binary_str = bin(int(num))[2:]
print("Binary representation: " + binary_str)
print("Enter position to find bit value: ")
p = int(input())
if(binary_str[p-1]=='1'):
    print("True")
else:
    print("False")
