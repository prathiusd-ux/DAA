
    
import csv
count=0
with open("Student.csv", "r") as f:
    read = csv.reader(f)
    
    next(read)
    for row in read:
        if "ai" in row[1]:
            count+=1
            print(f"row {count}:{row}")
    print("The number of times ai occurs is", count)
