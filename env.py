#!/usr/bin/python3
# A class for defining the concept of 'environment' which is related to the one of 'scope'
# The concept on 'env' contains more than just the 'items' we can currently see
# Also it uses the parent 'member', so it really is more than just the consecutive 
# function calls

class env:
    def __init__(self, parent=None, stdin=None, stdout=None, stderr=None):

        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.parent = parent

        if self.parent is not None:
            assert stdin is None
            assert stdout is None
            assert stderr is None
            self.stdin = parent.stdin
            self.stdout = parent.stdout
            self.stderr = parent.stderr

        self.items = {}

    # this function can really be usefull, it replaces some repetitive and 
    # verbose code
    def search(self, name):
        if name self.items:
            return self.items[name]
        elif self.parent is not None:
            return self.parent.search(name)
        else:
            return None

    # store new values into items by accessing directly the 'items' part
    # see if a certain value is in by accessing 'items' directly
