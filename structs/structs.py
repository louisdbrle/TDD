class FIFO:
    def __init__(self):
        self.first = [None, None]
        self.last = [None, None]

    def push(self, value):
        el = [value, None]
        if self.first[0] is None:
            self.first = el
            self.last = el
        else:
            self.last[1] = el
            self.last = el

    def pop(self):
        if self.first is None:
            return None
        else:
            value = self.first[0]
            self.first = self.first[1]
            return value


class LIFO:
    pass


class LILO:
    pass
