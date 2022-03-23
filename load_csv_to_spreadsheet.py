import openpyxl as px
import csv

wb = px.Workbook()

ws = wb.active

ws.title = "Airport Boardings"

with open('DATA/airport_boardings.csv') as airport_in:
    rdr = csv.reader(airport_in)
    for row in rdr:
        ws.append(row)

wb.save('airport_boardings.xlsx')

