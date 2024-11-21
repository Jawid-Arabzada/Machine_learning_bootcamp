rows = int(input("Enter ]the number of rows for the game board: "))
cols = int(input("Enter the number of columns for the game board: "))


row_hide = int(input(f"choose a row to hide the treasure (1-{rows})"))
if row_hide < 1 or row_hide > rows:
    print(f"invalid input! please enter a value betwen 1 and {rows}. ")
    row_hide = int(input(f"choose a row to hide the treasure (1-{rows})"))


col_hide = int(input(f"choose a col to hide the treasure (1-{cols})"))
if col_hide < 1 or col_hide > cols:
    print(f"invalid input! please enter a value betwen 1 and {cols}. ")
    col_hide = int(input(f"choose a col to hide the treasure (1-{cols})"))


row_hide -= 1
col_hide -= 1

for i in range(rows):
    for j in range(cols):
        if i == row_hide and j == col_hide:
            print("T", end=" ")
        else:
            print("*", end=" ")
    print()
