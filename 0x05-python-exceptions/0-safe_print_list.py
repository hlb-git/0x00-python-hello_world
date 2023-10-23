#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if (my_list):
        count = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                printed += 1
            except Exception:
                print()
                return (printed)
    print()
    return (printed)
