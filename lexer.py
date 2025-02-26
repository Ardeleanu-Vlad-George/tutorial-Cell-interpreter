#!/usr/bin/python3

source = "x=10;\ny=x+101;\nprint(\"This is the value:\"+y);\n"

isalpha = lambda chr: ('a' <= chr and chr <= 'z') or ('A' <= chr and chr <= 'Z')

isdigit = lambda chr: '0' <= chr and chr <= '9'

def literal_num(src, beg):
    result = ''
    while isdigit(src[beg]):
        result+=src[beg]
        beg+=1
    return result

def lex(src):
    for idx in range(len(src)):
        if src[idx] in " \n":
            continue
        elif src[idx] in "[]{}(),;:=":
            yield (src[idx], "")
        elif isalpha(src[idx]):
            yield ("alpha", src[idx])
        elif isdigit(src[idx]):
            value = literal_num(src, idx)
            print(idx)
            idx += len(value)
            print(idx)
            yield ("number", value)
        else:
            yield ("unknown", src[idx])
    else:
        yield ("eos", "") # eos - End Of Source


print("Source code after being tokenized:")
print(tuple(lex(source)))

