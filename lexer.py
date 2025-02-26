# the 'stream' class that will be used for progressing through the 
# 'source' data, the data that represents the text of the source file
import re
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
        print("Here's the next part:"+data_stream.next)
        result += data_stream.try_next()
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
            yield ("operation", ch)
        elif ch in "'\"":
            yield ("string", get_string(ch, strm))
        elif re.match("[.0-9]", ch):
            yield ("number", get_sequen(ch, strm, "[.0-9]"))
        elif re.match("[_a-zA-Z]", ch):
            yield ("identifier", get_sequen(ch, strm, "[_a-zA-Z0-9]"))
        elif ch == "\t":
            raise Exception("TAB is an illegal character inside Cell")
        else:
            raise Exception("Unidentified char detected")

    #if __name__ == "main":
src = "x=1;\ny=x+2;\nprint(y);"
src = "x=1;\ny=x+2;"
# for i in range(3):
#     print(tuple(lex(src)))
print(tuple(lex(src)))
