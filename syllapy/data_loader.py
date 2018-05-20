import csv


def load_dict():
    words = {}
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            words[row[0]] = row[1]
    return words
