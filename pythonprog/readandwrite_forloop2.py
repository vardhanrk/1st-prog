# program for reading and writing the data from excel file


import xlrd
import xlsxwriter
workbook = xlrd.open_workbook('dataxls4.xls')
worksheet = workbook.sheet_by_name('renu111')
totalrows = worksheet.nrows
totalcoloumns = worksheet.ncols
print("total rows", totalrows)
print("total cols:", totalcoloumns)
#code to create new excel file with the name resiltsfor2.xlsx
workbook1 = xlsxwriter.Workbook('resiltsfor2.xlsx')
# adding the sheet to work book and shete name as results sheet
worksheet1 = workbook1.add_worksheet("Resultssheet")




# dict_list = []
# reading the data from input excel file
worksheet1.write(0,totalcoloumns,'Results') # adding the header name as Results
for row_index in range(-1, totalrows):
    # print("ros")
    for col_index in range(0, totalcoloumns):
       # print(worksheet.cell(row_index, col_index).value)
       # writing the data to Resultsfor2 excel file
        worksheet1.write(row_index,col_index,worksheet.cell(row_index, col_index).value)
        
    # dict_list.append(d)

workbook1.close()
# print(dict_list)
print("finally Done!Results for xls file is created with values")
