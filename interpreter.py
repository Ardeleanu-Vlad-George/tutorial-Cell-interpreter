#!/usr/bin/python3
import sys
# import evaluator
import parser
import lexer

with open(sys.argv[1], 'r') as source:
    source = source.readlines()
    code = ''
    for line in source:
        code += line

print(code, end='')
