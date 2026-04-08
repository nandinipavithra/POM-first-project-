from xlrd import *

wb=open_workbook("C:\Users\Meghana\PycharmProjects\POM\generic_utility\excel.xlsx")
sh=wb.sheet_by_name("excel")
row=sh.row_values(0)
email=row[0]
pwd=row[1]

return email,pwd