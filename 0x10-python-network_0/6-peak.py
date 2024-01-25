#!/usr/bin/python3
""" finds the max number in list"""


def search(low, high, ints):
    mid = (low + high) // 2
    if low == high:
        return ints[high]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, high, ints))
    return(search(low, mid, ints))


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))
