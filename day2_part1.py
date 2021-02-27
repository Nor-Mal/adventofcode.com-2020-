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

        instances = found_pass.count(str(found_letter))

        if boundary_min <= instances and boundary_max >= instances:
            print('In the entry {} password is correct'.format(line))
            print('There are {} instances of letter {}\n'.format(instances,found_letter))
            total_passwords += 1
            #print('Total password:',total_passwords)
        else:
            print('In the entry {} password is incorrect'.format(line))
            print('There are {} instances of letter {}\n'.format(instances,found_letter))

    print('Number of correct passwords: {}\n'.format(total_passwords))
