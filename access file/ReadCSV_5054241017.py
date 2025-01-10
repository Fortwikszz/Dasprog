import csv
with open(r"D:\aaa\piton\dasprog\access file\chocolate.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)