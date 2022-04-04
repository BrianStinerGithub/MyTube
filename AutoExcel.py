import openpyxl as xl
from argparse import ArgumentParser

def update_sheet(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['Sheet1']

    corrected_price_cell = sheet.cell(1, 4)
    corrected_price_cell.value = "corrected price"
    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row, 3)
        corrected_price = cell.value * 0.9
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price
        
    wb.save(filename)


if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument("filename", help="The file or directory of files you want to update")
    args = parser.parse_args()
    update_sheet(args.filename)