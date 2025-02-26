class PeekableStream:
  def __init__(self, iterator):
    self.iterator = iter(iterator)
    self._fill()
  def _fill(self):
    try:
      self.next = next(self.iterator)
    except StopIteration:
      self.next = None
  def move_next(self):
    ret = self.next
    self._fill()
    return ret

def _scan(first_char, chars, allowed):
  ret = first_char
  p = chars.next
  while p is not None and re.match(allowed, p):
    ret += chars.move_next()
    p = chars.next
  return ret


strm = PeekableStream("x=1;\ny=3+x;\nprint(y);\n")
