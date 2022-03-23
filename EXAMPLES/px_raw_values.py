#!/usr/bin/env python
import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']  # <.>
    headers = next(ws.values)   # <.>
    for row in ws.values:  # <.>
        print(row[:3])   # <.>


if __name__ == '__main__':
    main()
