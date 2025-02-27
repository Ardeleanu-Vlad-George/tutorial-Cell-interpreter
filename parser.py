#!/usr/bin/python3
# this is the list of tokens we expect from the lexer, ordered based on the line of code
# to which they belong
avg_tok = (
    ('id', 'x'), ('=', ''), ('nr', '10'), (';', ''),
    ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''),
    ('id', 'print'), ('(', ''), ('sr', 'This is the result:'), ('op', '+'), ('id', 'y'), (')', ''), (';', '')
)

# here is a list of tokens that only do a simple assignment
ezy_tok = (
    ('id', 'x'), ('=', ''), ('nr', '-2.4'), (';', '')
)

