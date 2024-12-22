"""
SQL INTERACTION WITH PYTHON
Not Dynamic
"""


import sqlite3
import csv


def main():


    dbConnection = sqlite3.connect("RetirementData.db")
    dbCursor = dbConnection.cursor()

# Create 3 tables. Error exits.
    try:
        sCreateTable = ("CREATE TABLE "
                        "Employee(EmployeeID int, Name text)")
        dbConnection.execute(sCreateTable)

        sCreateTable = ("CREATE TABLE "
                        "Pay(EmployeeID int, Year int, Earnings real)")
        dbConnection.execute(sCreateTable)

        sCreateTable = ("CREATE TABLE "
                        "SocialSecurityMinimum(Year int, Minimum real)")
        dbConnection.execute(sCreateTable)

        dbConnection.commit()
    except sqlite3.OperationalError:
        print("Table already exists. "
              "Delete the database file to avoid error.")
        exit()


# Add records to the database
    with open("Employee.txt", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            sInsertPay = (f'INSERT INTO Employee(EmployeeID, Name) '
                          f'Values("{row[0]}", "{row[1]}")')
            dbConnection.execute(sInsertPay)
            dbConnection.commit()

    with open("Pay.txt", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            sInsertPay = (f'INSERT INTO Pay(EmployeeID, Year, Earnings) '
                          f'Values("{row[0]}", "{row[1]}", "{row[2]}")')
            dbConnection.execute(sInsertPay)
            dbConnection.commit()

    with open("SocialSecurityMinimum.txt", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            sInsertPay = (f'INSERT INTO SocialSecurityMinimum(Year, Minimum) '
                          f'Values("{row[0]}", "{row[1]}")')
            dbConnection.execute(sInsertPay)
            dbConnection.commit()


# Join the 3 tables and order by Name for output
    dbCursor.execute('SELECT a.Name, b.Year, b.Earnings, c.Minimum '
                     'FROM Employee AS a '
                     'JOIN Pay AS b '
                     'ON a.EmployeeID = b.EmployeeID '
                     'JOIN SocialSecurityMinimum AS c '
                     'ON b.Year = c.Year '
                     'ORDER BY a.Name')

# Output and concatenate last row based on Social Security inclusion
    print(
        f"{"Employee Name":<20}{"Year":<10}{"Earnings":<15}"
        f"{"Minimum":<15}{"Include":<10}")
    for row in dbCursor.fetchall():

        if row[2] >= row[3]:
            sResult = "Yes"
        else:
            sResult = "No"

        print(f"{row[0]:<20}{row[1]:<10}{row[2]:<15,.2f}"
              f"{row[3]:<15,.2f}{sResult:<10}")


if __name__ == "__main__":
    main()