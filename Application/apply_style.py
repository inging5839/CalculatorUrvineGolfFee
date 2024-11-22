import Calculator_time_fee as cal
from openpyxl import Workbook, load_workbook

def apply_style(df):
    wb = load_workbook('/Users/geon/Desktop/Golf_Cost_Auto_System/gathered.xlsx')
    ws = wb.active

    for row_idx, row_data in enumerate(df.itertuples(), start=2):
        ws.row_dimensions[row_idx].height = 15
    for column_idx, column_data in enumerate(df.items(), start=ord('A')):
        ws.column_dimensions[chr(column_idx)].width = 15

    for column_idx, column_data in enumerate(df.items(), start=ord('G')):
        ws.column_dimensions[chr(column_idx)].width = 8

    wb.save('/Users/geon/Desktop/Golf_Cost_Auto_System/gathered.xlsx')

