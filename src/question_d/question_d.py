#write functions here, don't add input('') statements here!

def multiplication_table(rows, cols):
    table = [[0] * cols for _ in range(rows)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            table[i-1][j-1] = i * j

    return table

def display_table(table):
    for row in table:
        print("\t".join(map(str, row)))

# Set the number of rows and columns for the table
rows = 10
cols = 10

# Generate the multiplication table
table = multiplication_table(rows, cols)

# Display the multiplication table
display_table(table)