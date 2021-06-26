with open('data.txt', 'r', ) as fp:
    total_yes = 0
    for answer in fp.read().split("\n\n"):
        x = set.intersection(*map(set, answer.split()))
        total_yes += len(list(x))
print(total_yes)
