#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {} - First character: {}".format(length, first))
