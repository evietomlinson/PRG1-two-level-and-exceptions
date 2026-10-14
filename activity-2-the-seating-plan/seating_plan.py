"""
Cinema Seating

A working program. The auditorium has five rows of eight seats.
X means booked, . means free. The program reports how full it is
and which rows still have space.

Row 0 is the front row.
"""

seats = [
    ["X", "X", ".", ".", ".", ".", "X", "X"],
    ["X", "X", "X", ".", ".", "X", "X", "X"],
    [".", ".", ".", ".", "X", ".", ".", "."],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    [".", ".", "X", "X", "X", "X", ".", "."],
]

ROWS = len(seats)
COLUMNS = len(seats[0])


def free_in_row(row):
    """How many free seats there are in one row."""
    free = 0
    for seat in row:
        if seat == ".":
            free = free + 1
    return free


def show_plan(seats):
    """Print the auditorium, front row first."""
    for row_number in range(ROWS):
        row_text = " ".join(seats[row_number])
        print(f"Row {row_number}:  {row_text}")


show_plan(seats)

total_seats = ROWS * COLUMNS
total_free = 0

print("---")
for row_number in range(ROWS):
    free = free_in_row(seats[row_number])
    total_free = total_free + free
    print(f"Row {row_number}: {free} free")

print("---")
print(f"{total_seats - total_free} of {total_seats} seats sold")
print(f"{total_free} still available")
 

most_seats = -1
best_row = 0

for row_number in range(ROWS):
    free = free_in_row(seats[row_number])

    if free > most_seats:
        most_seats = free
        best_row = row_number

print(f"Row with most seats available: {best_row}")

print("---")
for row_number in range(0,2):
    free = free_in_row(seats[row_number])
    total_free = total_free + free
    print(f"Row {row_number}: {free} free")
    
print("---")
column_one = 0 
for row_number in range(ROWS):
    if seats[row_number][0] == ".":
        column_one += 1 

print(column_one)