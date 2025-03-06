#!/usr/bin/python3

# It does what it's name suggests, it creates an object with the 
# behaviour of a 'stack', but without the 'put' method
class no_put_stack:
    def __init__(self, data):
        self.one_time_copy = iter(data)
        self.mov_next()

    # 'try' moving forward, update 'next' accordingly
    def mov_next(self):
        try:
            self.next = next(self.one_time_copy)
        except StopIteration:
            self.next = None

    # 'cut' the next from the data, try moving forward
    def pop_next(self):
        result = self.next
        self.mov_next()
        return result


if __name__ == "__main__":
    data = ['r', 'more data', ('a','tuple','with numbers', 34, 4.2, -.2), [4, 0], 3]
    nps = no_put_stack(data)
    while nps.next is not None:
        print(nps.pop_next())
