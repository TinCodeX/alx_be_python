size = int(input("Enter the size of the pattern: "))
row = 0  # Initialize row counter

while row < size:
    for col in range(size):
        print("*", end="")  # Print '*' without newline
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
