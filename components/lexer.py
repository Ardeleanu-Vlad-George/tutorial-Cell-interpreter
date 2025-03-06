#!/usr/bin/python3
import re
from lib.no_put_stack import no_put_stack as nps

def get_string(quote_type, char_stack):
    result = ""
    while char_stack.next != quote_type:
        ch = char_stack.pop_next()
        result += ch
    char_stack.pop_next()
    return result

def get_sequen(seq_beg, char_stack, seq_allowed):
    result = seq_beg
    nxt = char_stack.next
    while nxt is not None and re.match(seq_allowed, nxt):
        result += char_stack.pop_next()
        nxt = char_stack.next 
    return result

def lex(source):
    stack = nps(source)
    while stack.next is not None:
        ch = stack.pop_next()
        if ch in " \n\t": # Ignore the white spaces
            pass
        elif ch in "(){},;:=": # Special tokens
            yield (ch, "")
        elif ch in "+*-/":
            yield ("op", ch)
        elif ch in "'\"":
            yield ("sr", get_string(ch, stack))
        elif re.match("[.0-9]", ch):
            yield ("nr", get_sequen(ch, stack, "[.0-9]"))
        elif re.match("[_a-zA-Z]", ch):
            yield ("id", get_sequen(ch, stack, "[_a-zA-Z0-9]"))
        # no ending 'else' needed, no errors are expected


if __name__ == "__main__":
    src = "x=10;\ny=x+101;\nMSG=\"This is the result:\";\nprint(MSG, y);\n"
    print("Tokens in one tuple:", tuple(lex(src)))
    tok_stck = nps(lex(src))
    print("Tokens separated")
    while tok_stck.next is not None:
        print(tok_stck.pop_next())
