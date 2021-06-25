with open('./data.txt', 'r', ) as fp:
    entry = []
    sum_yes = 0
    for answer in fp.read().split("\n"):
        if answer != '':
            [entry.append(x) for x in answer if x not in entry]
        else:
            sum_yes += len(entry)
            entry = []
print(sum_yes)
