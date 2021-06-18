'''
Advent of Code 2020 - Day5 Part1 solution in Python

F - front seats, keep lower half
B - back seats, keep upper half
L - left side, keep lower half
R - right side, keep upper half

0 - 127  (128 rows of seats)
0 - 7 (8 columns of seats)

'''
import re

with open('./data.txt', 'r',) as fp:
	data = list(fp.read().splitlines())
	
seat_id_list = []

for code in data:
  
    row_start, row_end = 0, 127
    column_start, column_end = 0, 7
    
    for char in code:
        if char == 'F':
            row_start, row_end = row_start, ((row_end - row_start)//2 + row_start)
            # print("Letter was {} and range was {} to {}".format(char, row_start, row_end))
            
        elif char == 'B':
            row_start, row_end = row_start + ((row_end - row_start+1)//2), row_end
            # print("Letter was {} and range was {} to {}".format(char, row_start, row_end))
            
        elif char == 'R':
            column_start, column_end = column_start + ((column_end - column_start+1)//2), column_end
            # print("Letter was {} and range was {} to {}".format(char, column_start, column_end))
            
        elif char == 'L':
            column_start, column_end = column_start, ((column_end - column_start)//2 + column_start)
            # print("Letter was {} and range was {} to {}".format(char, column_start, column_end))
            
    # print("Final row = {}".format(row_end))
    # print("Final column = {}".format(column_end))

    seat_id = (row_end*8)+column_end
    # print("Seat ID: {}".format(seat_id))
    seat_id_list.append(seat_id)
    
print("Highest seat ID = {}".format(max(seat_id_list)))
