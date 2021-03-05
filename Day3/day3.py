# Advent of Code 2020 - day3 solution to part1 and part2
# Works but it is very slow solution compared to other that you can find on the
# web which use the list comprehensions. That was me without looking
# for any help on the web - I am not impressed with myself ;-)

with open('map_entry_day3.txt') as fp:
    line = fp.read().splitlines()

    tdd_list_ori = []

    for c in range(0, len(line)):
        in_line = list(line[c])
        tdd_list_ori.insert(c, in_line)

        ori = tdd_list_ori

    # function that extends 'ori_list' by 'num' times and returns modified 'mod_list'
    def list_multi(ori_list, num):
        """
        :param ori_list: takes 2D list to be multiplied
        :param num: how many time to multiply list
        :return: column vector multiplication of the entry 2D list (ori_list)
        """
        mod_list = [[] for _ in range(len(ori_list))]
        k = 0

        while k < num:
            for i in range(len(ori_list)):
                for j in range(len(ori_list[i])):
                    mod_list[i].extend(ori_list[i][j])
            k += 1
        return mod_list

    # function that takes two-dimensional list 'dd_list' and checks how many '#' can be found
    # with a given steps to the 'right' and 'down'
    def check_slope(dd_list, right, down):
        """
        :param dd_list: takes list to check
        :param right: int as column vector step
        :param down: int as row vector step
        :return: total number of the checked list positions that equalled to '#'
        """
        counter = 0
        row = 0
        col = 0
        x = 1

        for i in range(len(dd_list)):
            for j in range(len(dd_list[0])):
                if row >= len(dd_list):
                    break
                else:
                    if col >= len(dd_list[0]):
                        dd_list = list_multi(ori, x)
                        x += 1
                        row -= down
                        col -= right
                    else:
                        if dd_list[row][col] == '#':
                            dd_list[row][col] = 'X'
                            counter += 1
                        else:
                            dd_list[row][col] = 'O'
                row += down
                col += right
        return counter


    new_list = list_multi(ori, 1)
    print('Please wait... :-(')
    s_one = check_slope(new_list, 1, 1)
    s_two = check_slope(new_list, 3, 1)
    s_three = check_slope(new_list, 5, 1)
    s_four = check_slope(new_list, 7, 1)
    s_five = check_slope(new_list, 1, 2)

    print(s_two)
    print(s_one * s_two * s_three * s_four * s_five)
