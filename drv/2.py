# @brief This file contains implementation of two independent discrete random variables addition
# @author Iskandar Gabdrakhmanov
# Usage example: script_name -v1 "[1-1/4,2-1/4,3-1/2]" -v2 "[1-1/3,2-2/3]"

import sys
import re
from fractions import Fraction
from prettytable import PrettyTable

# x = [[1, Fraction(2, 6)], [2, Fraction(1, 6)], [3, Fraction(3, 6)]]
# y = [[1, Fraction(1, 7)],[2, Fraction(2, 7)],[3, Fraction(4, 7)]]

def check_list(list_arg):
    list_arg = re.sub(r'\s', '', list_arg)
    pattern = re.compile(r'\[*(\d+-\d+/?\d*,)+(\d+-\d+/?\d*)\]')
    if pattern.findall(list_arg):
        return True
    return False


def check_num_of_args(args):
    if len(args) == 5:
        return True
    else:
        return False


def print_usage(usage_type):
    if usage_type == 1:
        print("Usage example: script_name -v1 \"[1-1/4,2-1/4,3-1/2]\" -v2 \"[1-1/3,2-2/3]\"")
    elif usage_type == 2:
        print("The sum of the probabilities of the random variable must equal to 1")


def check_args(args):
    if check_num_of_args(args) is True:
        if args[1] == '-v1' and args[3] == '-v2':
            if check_list(args[2]) is True and check_list(args[4]) is True:
                return True
    return False


def parse_list_of_variables(list_in):
    initial = str(list_in[1:-1]).split(',')
    final_list = []
    for i in initial:
        temp = i.split('-')
        t1 = int(temp[0])
        t2 = Fraction(temp[1])
        final_list.append([t1, t2])
    return final_list


# check if the probabilities in sum equal to 1
def check_probabilities(list_in):
    sum_of_probabilities = Fraction()
    for i in list_in:
        sum_of_probabilities += i[1]
    if sum_of_probabilities == 1:
        return True
    return False


def separate_events_and_probabilities(t, s):
    if s == "A":
        a = ["A"]
    else:
        a = ["B"]
    ap = ["P"]
    for i in t:
        a.append(i[0])
        ap.append(i[1])
    return a, ap


def print_table(t, tp):
    table_t = PrettyTable(t)
    table_t.add_row(tp)
    print(table_t)
    return table_t


def add_two_variables(a, b):
    ab = ["A+B"]
    abp = ["P"]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i][0] + b[j][0] not in ab:
                ab.append(a[i][0] + b[j][0])
                abp.append(a[i][1] * b[j][1])
            else:
                index_in = ab.index(a[i][0] + b[j][0])
                abp[index_in] += a[i][1] * b[j][1]
    a, ap = separate_events_and_probabilities(a, "A")
    b, bp = separate_events_and_probabilities(b, "B")
    print_table(a, ap)
    print_table(b, bp)
    table_abp = print_table(ab, abp)
    print("--" * sum(table_abp._widths))


def main():
    if check_args(sys.argv) is False:
        print_usage(1)
        return
    v1 = parse_list_of_variables(sys.argv[2])
    v2 = parse_list_of_variables(sys.argv[4])
    if check_probabilities(v1) is True and check_probabilities(v2) is True:
        add_two_variables(v1, v2)
    else:
        print_usage(2)


main()




