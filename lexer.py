source = "x=1;\ny=x+3;\nprint(y);\n"

def isalpha(chr):
    return ('a' <= chr and chr <= 'z') or ('A' <= chr and chr <= 'Z')

def isdigit(chr):
    return '0' <= chr and chr <= '9'

def lex(src):
    for idx in range(len(src)):
        if src[idx] in " \n":
            continue
        elif src[idx] in "[]{}(),;:=":
            yield (src[idx], "")
        elif isalpha(src[idx]):
            yield ("alpha", src[idx])
        elif isdigit(src[idx]):
            yield ("digit", src[idx])
        else:
            yield ("unknown", src[idx])


print("Source code after being tokenized:")
print(tuple(lex(source)))

