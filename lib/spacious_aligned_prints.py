#!/usr/bin/python3
import cmd 

if __name__ == '__main__':
    toks = (('id', 'x'), ('=', ''), ('nr', '10'), (';', ''), ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''), ('id', 'MSG'), ('=', ''), ('sr', 'This is the result:'), (';', ''), ('id', 'print'), ('(', ''), ('id', 'MSG'), (',', ''), ('id', 'y'), (')', ''), (';', ''))
    str_toks = tuple(str(toks[_]) for _ in range(len(toks)))
    # print(str_toks)
    # cmd.Cmd.columnize(list(str_toks))
    c = cmd.Cmd()
    c.columnize(str_toks)
    print('Running in main')

(('id', 'x'), ('=', ''), ('nr', '10'), (';', ''), ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''), ('id', 'MSG'), ('=', ''), ('sr', 'This is the result:'), (';', ''), ('id', 'print'), ('(', ''), ('id', 'MSG'), (',', ''), ('id', 'y'), (')', ''), (';', ''))
(('asgn', ('id', 'x'), ('nr', '10')), ('asgn', ('id', 'y'), ('comp', '+', ('id', 'x'), ('nr', '101'))), ('call', ('id', 'print'), [('comp', '+', ('sr', 'This is the result:'), ('id', 'y'))]))
