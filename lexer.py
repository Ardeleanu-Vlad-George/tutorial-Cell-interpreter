#!/usr/bin/python3
import re

# the 'stream' class that will be used for progressing through the 
# 'source' data, the data that represents the text of the source file

# A class serving a similar purpose to the 'std::stringstream' of C++
class stream:
    def __init__(self, source):
        self.iterator = iter(source)
        self.try_next()

    # 'try' moving forward, update 'next' accordingly
    def try_next(self):
        try:
            self.next = next(self.iterator)
        except StopIteration:
            self.next = None

    # 'cut' the next from the data, try moving forward
    def cut_next(self):
        result = self.next
        self.try_next()
        return result

isdigit = lambda ch: '0' <= ch and ch <= '9'

isletter= lambda ch: ('a' <= ch and ch <= 'z') or ('A' <= ch and ch <= 'Z') 

def get_string(quote_type, data_stream):
    result = ""
    while data_stream.next != quote_type:
        ch = data_stream.cut_next()
        if ch is None:
            raise Exception("No equivalent quotiation mark was found")
        result += ch
    data_stream.cut_next()
    return result

def get_sequen(seq_beg, data_stream, seq_allowed):
    result = seq_beg
    nxt = data_stream.next
    while nxt is not None and re.match(seq_allowed, nxt):
        result += data_stream.cut_next()
        # result += data_stream.try_next() 
        # the above lien was causing an error, you thought that the implementation
        # of 'try_next' was to blame, except it wasn't for 'try_next' shouldn't 
        # return anything. Once you called the proper function, 'cut_next' 
        # it worked properly
        nxt = data_stream.next 
    return result

def lex(source_code):
    strm = stream(source_code)
    while strm.next is not None:
        ch = strm.cut_next()
        if ch in " \n": # Ignore the white cases
            pass
        elif ch in "(){},;:=": # Special tokens
            yield (ch, "")
        elif ch in "+*-/":
            yield ("op", ch)
        elif ch in "'\"":
            yield ("sr", get_string(ch, strm))
        elif isdigit(ch):
            yield ("nr", get_sequen(ch, strm, "[.0-9]"))
        elif re.match("[_a-zA-Z]", ch):
            yield ("id", get_sequen(ch, strm, "[_a-zA-Z0-9]"))
        elif ch == "\t":
            raise Exception("TAB is an illegal character inside Cell")
        else:
            raise Exception("Unidentified char detected")
    else:
        yield ("eos", "")

    #if __name__ == "main":
if __name__ == "__main__":
    source = "x=10;\ny=x+101;\nprint(\"This is the result:\" + y);"
    print(tuple(lex(source)))
