from openpyxl import load_workbook


def load_list_from_sheet_by_col(filename : str, sheet_index : int, col_index: int):
    result = []

    workbook = load_workbook(filename)

    worksheet = workbook[workbook.sheetnames[sheet_index]]
    # header = worksheet.cell(1, col_index).value
    for row in range(1, worksheet.max_row + 1):
        result.append(worksheet.cell(row, col_index).value)

    return result
