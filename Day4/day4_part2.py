# Advent of Code 2020 - Day4-Part2 solution in Python
import re

with open('pass_entry.txt', 'r',) as fp:
	intake = fp.readlines()

# Below code formats the entry data to a list of different strings,
# where each string represents one passport and each info is shown
# in a dictionary format (key:value) with a white space between them.

new_list = [' '.join(intake)][0].split(' \n ')

new_list = [x.replace('\n', '') for x in new_list]

# below code takes above list and changes her each element
# to a dictionary with keys and values

match_list = []
check_key = []
check_value = []

for r in range(0, len(new_list)):
	check_key.append(re.findall(r'\w\w\w(?=\:)',new_list[r]))
	check_value.append(re.findall(r'(?<=\:)[^\. ]+',new_list[r]))

for i in range(0 , len(check_key)):
	d = {}
	for j in range(0, len(check_key[i])):
		d.update({check_key[i][j]:check_value[i][j]})
	match_list.append(d)

#functions that check the rules for the valid passports
def validate_one(x):
	byr = int(x['byr'])
	iyr = int(x['iyr'])
	eyr = int(x['eyr'])

	if (byr >= 1920 and byr <= 2002) and (iyr >= 2010 and iyr <= 2020)\
		and (eyr >= 2020 and eyr <= 2030):
		return True
	else:
		return False

def validate_two(x):
	entry_hgt = re.findall(r'(cm|in)', x['hgt'])
	entry_hgt_val = re.findall(r'\d+', x['hgt'])
	hgt_val = int(entry_hgt_val[0])

	if entry_hgt != []:
		if entry_hgt[0] == 'cm':
			if hgt_val >= 150 and hgt_val <= 193:
				return True
			else:
				return False
		elif entry_hgt[0] == 'in':
			if hgt_val >= 59 and hgt_val <= 76:
				return True
			else:
				return False
	else:
		return False

def validate_three(x):
	hcl = x['hcl']
	val_char = ['a' , 'b', 'c', 'd', 'e', 'f', '0',
	 			'1', '2', '3', '4', '5', '6', '7', '8', '9']
	matched = [characters in val_char for characters in hcl[1::]]

	if hcl[0] == '#' and len(hcl[1::]) == 6:
		valid_string = all(matched)
		return valid_string
	else:
		return False

def validate_four(x):
	ecl = x['ecl']
	if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return True
	else:
		return False

def validate_five(x):
	pid = x['pid']
	if len(pid) == 9:
		return True
	else:
		return False

# Main program
keys = ['byr', 'cid', 'ecl', 'eyr','hcl', 'hgt', 'iyr', 'pid']
no_cid  = ['byr', 'ecl', 'eyr','hcl', 'hgt', 'iyr', 'pid']

counter = 0
for x in match_list:
	num = list(x.keys())
	num.sort()
	if num == keys or num == no_cid:
		if validate_one(x) and validate_two(x) and validate_three(x)\
		   and validate_four(x) and validate_five(x):
			counter += 1
	else:
		pass
print("Total valid passports:",counter)
