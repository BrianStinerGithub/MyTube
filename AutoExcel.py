import os
import openpyxl as xl
from argparse import ArgumentParser
from os import path
from threading import Thread

def update_sheet(file):
    try:
        wb = xl.load_workbook(file)
        ws = wb.active
        ws.cell(row=1, column=1).value = 'Updated'
        wb.save(file)
    except FileNotFoundError:
        print('File not found: {}'.format(file))
    except PermissionError:
        print('Permission denied: {}'.format(file))
    except Exception as e:
        print('Error: {}'.format(e))

def get_files(filename):
    try:
        if path.isdir(filename):
            return [f for f in os.listdir(filename) if f.endswith('.xlsx')]
        if path.isfile(filename) and filename.endswith('.xlsx'):
            return [filename]
    except FileNotFoundError:
        print('File not found: {}'.format(filename))

def main(filename):
    files = get_files(filename)

    threads = []
    for file in files:
        t = Thread(target=update_sheet, args=(file,))
        t.start()
        threads.append(t)
    threads = [t.join() for t in threads]
    print('Done')
        


if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument("filename", help="The file or directory of files you want to update")
    args = parser.parse_args()
    main(args.filename)