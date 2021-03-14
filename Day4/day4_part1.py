# Advent of Code 2021 - Day4 Part1 solution in Python
import re

with open('pass_entry.txt', 'r',) as fp:
	intake = fp.readlines()

new_list = [' '.join(intake)][0].split(' \n ')

new_list = [x.replace('\n', '') for x in new_list]

valid_one = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid', 'cid']
valid_two = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']

valid_one.sort()
valid_two.sort()

match_list = []

for x in range(0, len(new_list)):
	check = re.findall(r'\w\w\w(?=\:)',new_list[x])
	match_list.append(check)
	match_list[x].sort()

counter = 0

for r in range(0, len(match_list)):
	if match_list[r] == valid_one or match_list[r] == valid_two:
		counter += 1

print('Total of valid passwords:',counter)
