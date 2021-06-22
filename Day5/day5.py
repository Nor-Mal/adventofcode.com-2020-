'''
Advent of Code 2020 - Day5 Part1 solution in Python

F - front seats, keep lower half
B - back seats, keep upper half
L - left side, keep lower half
R - right side, keep upper half

0 - 127  (128 rows of seats)
0 - 7 (8 columns of seats)

'''
# - PART 1 -
with open('./data.txt', 'r',) as fp:
	data = list(fp.read().splitlines())
	
seat_id_list = []

for code in data:
  
    row_start, row_end = 0, 127
    column_start, column_end = 0, 7
    
    for char in code:
        if char == 'F':
            row_start, row_end = row_start, ((row_end - row_start)//2 + row_start)
            
        elif char == 'B':
            row_start, row_end = row_start + ((row_end - row_start+1)//2), row_end
            
        elif char == 'R':
            column_start, column_end = column_start + ((column_end - column_start+1)//2), column_end
            
        elif char == 'L':
            column_start, column_end = column_start, ((column_end - column_start)//2 + column_start)

    seat_id = (row_end*8)+column_end
 
    seat_id_list.append(seat_id)
    
print("Highest seat ID = {}".format(max(seat_id_list)))

# - PART 2 -
for item in range(len(seat_id_list)-1):
    if seat_id_list[item+1] - seat_id_list[item] != 1:
        print("Your seat ID: {}".format(seat_id_list[item]+1))


