# Importing required libraries which is required
import xlrd
import sqlite3

# Establish a SQLite3 connection & creating database
conn = sqlite3.connect("ImportingData.db")

# Creating cursor 
cur = conn.cursor()

class ImportingData_Excel_Database:
    def __init__(self):
        
        # Open the workbook and define the worksheet
        self.book = xlrd.open_workbook("Important Documents/Programming Books.xls")
        self.sheet = self.book.sheet_by_name("BookDetails")

        # Calling function to run the further lines of code
        self.ImportingData()

    def ImportingData(self):
        
        # Create Table
        self.product_details_table = ("create table if not exists Excel_Database(sr_no text, books_name text, author_name text)")
        print("Table has been Created..")

        # Execute create table query
        cur.execute(self.product_details_table)

        # Create the INSERT INTO SQL query
        self.query = ("insert into Excel_Database values (?,?,?)")

        # Create a For loop to iterate through each row in the XLS file
        for r in range(1,self.sheet.nrows):
            self.sr_no = self.sheet.cell(r,0).value
            self.book_name = self.sheet.cell(r,1).value
            self.author_name = self.sheet.cell(r,2).value

            # Assign values from each row        
            self.values = (self.sr_no, self.book_name, self.author_name)

            # Execute sql Query
            cur.execute(self.query, self.values)

        # Close the cursor
        cur.close()

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        # Print results
        print("Data has been Added Successfully")
    
if __name__ == "__main__":
    # Creating object of the class
    obj = ImportingData_Excel_Database()