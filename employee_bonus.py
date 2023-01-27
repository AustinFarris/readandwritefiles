import csv


def main():
    infile = open("EmployeePay.csv", "r")

    reader = csv.reader(infile)

    for row in reader:
        print(*row)


if __name__ == "__main__":
    main()
