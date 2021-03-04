#  --- Day 1: Report Repair ---
#  --- Part 1

with open('data_entry.txt', 'r') as fp:
    entry = fp.read().splitlines()

    data_entry = []
    for i, j in enumerate(entry):
        a = entry[i]
        data_entry.append(int(a))

result = []

for x in data_entry:
    for y in data_entry:

        numbers_added = x + y

        if numbers_added == 2020:
            numbers_multi = x * y
            result.append(x)


print('Two found entries: {}'.format(result))

print('Answer: {}'.format(numbers_multi))
