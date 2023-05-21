#printing Numbers in Right Angle Triangle shape

n = int (input("Enter the number of rows:"))

for i in range (1, n+1) :
    for j in range (1, i+1):
        print(j, end="")      #switch j with i for identical numbers for each row
    print()

