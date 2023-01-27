import csv
import os


def main():
    infile = open("sales.csv", "r")
    outfile = open("salesreport.csv", "w+")

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        report_list = [row[0], row[3]]
        writer.writerow(report_list)


if __name__ == "__main__":
    main()
