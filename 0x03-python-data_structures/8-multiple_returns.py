#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence) - 1
    return (len(sentence), "None" if i < 0 else sentence[0])
