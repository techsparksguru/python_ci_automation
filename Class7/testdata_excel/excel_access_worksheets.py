from openpyxl import Workbook,load_workbook

wb = load_workbook(filename='TestExcel.xlsx')

## Sheets within the above workbook can be loaded in below two methods

# This method is depricated by openpyxl, meaning this won't be maintained going forward
ws_method1 = wb.get_sheet_by_name('Sheet') 
print(ws_method1.title)

# This is the preffered method that can be used to change the active sheet
# Syntax: wb['Yoursheetname']
ws_method2 = wb['sheet_title'] 
print(ws_method2.title)
