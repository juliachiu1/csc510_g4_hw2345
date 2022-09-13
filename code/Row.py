class Row:
    def __init__(self, t):
        self.cells = t
        self.cooked = t.deepcopy()
        self.isEvaled = False