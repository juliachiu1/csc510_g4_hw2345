from Csv import Csv

class Col:
    def __init__(self):
        file = Csv()
        file.read_csv()
        self.names = file.data[0][:]
        self.x = []
        self.y = []

    def new(self):
        for items in self.names:
            if "+" in items or "-" in items:
                self.y.append(items)
            elif":" in items:
                continue
            else:
                self.x.append(items)

        #print(self.x)
        #print(self.y)


#test = Col()
#test.new()

