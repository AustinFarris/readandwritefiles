import csv
import os


def main():
    infile = open("sales.csv", "r")
    outfile = open("salesreport.csv", "w+")

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    end_line = reader

    fieldnames = ["Customer | Total"]
    writer.writerow(fieldnames)

    next(reader)
    total = 0
    new_id = ""
    row_num = 0

    for row in reader:

        if row[0] == new_id or "":
            total += float(row[3]) + float(row[4]) + float(row[5])
            new_id = row[0]
            row_num += 1
            if row_num == 79:
                output_list = [new_id, format(total, ".2f")]
                writer.writerow(output_list)
        elif row[0] != new_id:
            output_list = [new_id, format(total, ".2f")]
            if total != 0:
                writer.writerow(output_list)
            new_id = row[0]
            total += float(row[3]) + float(row[4]) + float(row[5]) - total
            row_num += 1

    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
