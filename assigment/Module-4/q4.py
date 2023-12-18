def print_number_pattern(rows):
    current_number = 1

    for i in range(1, rows + 1):
        # Print spaces
        for j in range(1, rows - i + 1):
            print(" ", end=' ')

        # Print numbers
        for k in range(1, i + 1):
            print(current_number, end=' ')
            current_number += 1

        # Move to the next line after each row
        print()

# Get user input for the number of rows
num_rows = int(input("Enter the number of rows: "))

# Print the pattern
print_number_pattern(num_rows)
