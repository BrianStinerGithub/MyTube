import os
import argparse
import random 
import openpyxl 
import threading

def fill_folder(directory, num=10):
    """
    Fills a folder with num empty excel files
    """
    files = os.listdir(directory)
    excel_files = [file for file in files if file.endswith('.xlsx')]
    for i in range(num):
        file_name = 'file' + str(i) + '.xlsx'
        if file_name not in excel_files:
            wb = openpyxl.Workbook()
            wb.save(file_name)

def excel_folder(directory):
    """
    Each excel file in the directory gets a thread to run process_excel
    """
    files = os.listdir(directory)
    excel_files = [file for file in files if file.endswith('.xlsx')]
    threads = []
    for file in excel_files:
        t = threading.Thread(target=process_excel, args=(file,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def process_excel(file_name):
    """
    Adds random data to the excel file and saves it
    """
    with open(file_name, 'r') as f:
        wb = openpyxl.load_workbook(f)
        sheet = wb.active
        rows = sheet.rows
        for row in rows:
            for cell in row:
                cell.value = random.randint(-100, 100)*random.random()
        wb.save(file_name)


def main():
    parser = argparse.ArgumentParser(description='File or folder of excel files are filled with random data')
    parser.add_argument('-f', '--file', help='File or directory of files to be filled with random data')
    args = parser.parse_args()
    if args.file:
        if os.path.isdir(args.file):
            excel_folder(args.file)
        elif os.path.isfile(args.file):
            process_excel(args.file)
        else:
            print('File or directory not found')
    else:
        print('Need a file or directory as an argument')

if __name__ == "__main__":
    main()