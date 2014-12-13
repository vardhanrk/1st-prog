# program for reading and writing the data from excel file


import xlrd
import xlsxwriter
workbook = xlrd.open_workbook('dataxls3.xls')
worksheet = workbook.sheet_by_name('renu')
totalrows = worksheet.nrows - 1
totalcoloumns = worksheet.ncols - 1
print("total rows", totalrows)
print("total cols:", totalcoloumns)
workbook1 = xlsxwriter.Workbook('resiltsfor.xlsx')
worksheet1 = workbook1.add_worksheet()




# dict_list = []
worksheet1.write(0,totalcoloumns,'Results')
for row_index in range(-1, totalrows):
    # print("ros")
    for col_index in range(-1, totalcoloumns):
        print(worksheet.cell(row_index, col_index).value)
        worksheet1.write(row_index,col_index,worksheet.cell(row_index, col_index).value)
        
   # dict_list.append(d)
workbook1.close()
# print(dict_list)
print("finally Done!Refults for xls file ia created with values")
