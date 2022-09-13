from Csv import Csv

class Col:
    def __init__(self):
        self.file = Csv()
        self.file.read_csv()
        self.names = self.file.data[0][:]
        self.x = []
        self.y = []
        self.at = {}

    def new(self):
        for i,items in enumerate(self.names):
            if "+" in items or "-" in items:
                self.y.append(items)
            elif":" in items:
                continue
            else:
                self.x.append(items)
            self.at[items] = i + 1

        #print(self.x)
        #print(self.y)


#test = Col()
#test.new()
