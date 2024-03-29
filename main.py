import os
from sys import argv

script, client_folder, retailer_folder, start_date, end_date = argv

def main():
    format=r"python C:\Users\python\Desktop\SalesInvoiceAnalysis\src\Sales_Invoice_Analysis.py {} {} {} {}"
    os.system(format.format(client_folder,retailer_folder,start_date,end_date))
    print("Pricing Claims have been uploaded to the database.")

if __name__ == "__main__":
    main()