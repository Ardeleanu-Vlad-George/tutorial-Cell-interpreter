#!/usr/bin/python3
import re
from no_put_stack import no_put_stack as nps
# import no_put_stack.no_put_stack as nps

isdigit = lambda ch: '0' <= ch and ch <= '9'

isletter= lambda ch: ('a' <= ch and ch <= 'z') or ('A' <= ch and ch <= 'Z') 

def get_string(quote_type, char_stack):
    result = ""
    while char_stack.next != quote_type:
        ch = char_stack.pop_next()
        if ch is None:
            raise Exception("No equivalent quotiation mark was found")
        result += ch
    char_stack.pop_next()
    return result

def get_sequen(seq_beg, char_stack, seq_allowed):
    result = seq_beg
    nxt = char_stack.next
    while nxt is not None and re.match(seq_allowed, nxt):
        result += char_stack.pop_next()
        # result += char_stack.mov_next() 
        # the above lien was causing an error, you thought that the implementation
        # of 'mov_next' was to blame, except it wasn't for 'mov_next' shouldn't 
        # return anything. Once you called the proper function, 'pop_next' 
        # it worked properly
        nxt = char_stack.next 
    return result

def lex(source):
    stack = nps(source)
    while stack.next is not None:
        ch = stack.pop_next()
        if ch in " \n": # Ignore the white cases
            pass
        elif ch in "(){},;:=": # Special tokens
            yield (ch, "")
        elif ch in "+*-/":
            yield ("op", ch)
        elif ch in "'\"":
            yield ("sr", get_string(ch, stack))
        elif isdigit(ch):
            yield ("nr", get_sequen(ch, stack, "[.0-9]"))
        elif re.match("[_a-zA-Z]", ch):
            yield ("id", get_sequen(ch, stack, "[_a-zA-Z0-9]"))
        elif ch == "\t":
            raise Exception("TAB is an illegal character inside Cell")
        else:
            raise Exception("Unidentified char detected")


if __name__ == "__main__":
    src = "x=10;\ny=x+101;\nprint(\"This is the result:\" + y);"
    dt = iter(lex(src))
    print(dt.__next__())
    print(dt.__next__())
    print(tuple(lex(src)))
