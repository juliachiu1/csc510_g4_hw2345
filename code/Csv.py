import csv


def read_csv(filename):
    # Open file
    with open(filename) as file_obj:
        # Skips the heading
        # Using next() method

        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)

        count = 0
        data = []

        # Iterate over each row in the csv file
        # using reader object
        for row in reader_obj:
            data.append(row)
            count += 1
        #print(data)
