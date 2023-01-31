import csv


def main():
    infile = open("customers.csv", "r")
    outfile = open("customer_country.csv", "w+")

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        cust_name = row[1]
        cust_coun = row[4]
        cust_list = (cust_name, cust_coun)

        writer.writerow(cust_list)

    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
