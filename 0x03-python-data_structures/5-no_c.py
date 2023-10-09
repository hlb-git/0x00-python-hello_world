#!/usr/bin/python3
def no_c(my_string):
    i = ''
    return (i.join(x for x in my_string if x not in 'Cc'))
