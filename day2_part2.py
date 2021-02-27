import os, re

file_dir = os.getcwd()

with open("{}\entry_for_day2.txt".format(file_dir)) as fp:
    mylist = fp.read().splitlines()

    total_passwords = 0

    for line in mylist:

        boundary = re.search(r'^\d+-\d+',line)
        boundary_min = int(boundary.group().split('-')[0])
        boundary_max = int(boundary.group().split('-')[1])

        letter_to_find = re.search(r'.:',line)
        found_letter = letter_to_find.group().split(':')[0]

        pass_to_find = re.search(r'(?<=:\s).+',line)
        found_pass = pass_to_find.group()
        letters = list(found_pass)

        if letters[boundary_min-1] == found_letter and letters[boundary_max-1] != found_letter or letters[boundary_min-1] != found_letter and letters[boundary_max-1] == found_letter :
            print('{} is valid'.format(line))
            total_passwords += 1
        else:
            print('{} is invalid'.format(line))

    print('Total number of valid passwords: {}\n'.format(total_passwords))
