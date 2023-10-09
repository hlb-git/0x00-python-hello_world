#!/usr/bin/python
def multiple_returns(sentence):
    if (len(sentence) > 0):
        return ((len(sentence), sentence[0]))
    return ((len(sentence), None))
