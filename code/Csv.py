import csv


class Csv:
    def __init__(self):
        self.filename = '../data/auto93.csv'
        self.count = 0
        self.data = []

    def read_csv(self):
        # Open file
        with open(self.filename) as file_obj:
            # Skips the heading
            # Using next() method

            # Create reader object by passing the file
            # object to reader method
            reader_obj = csv.reader(file_obj)

            # Iterate over each row in the csv file
            # using reader object
            for row in reader_obj:
                self.data.append(row)
                self.count += 1
        return self.data                
