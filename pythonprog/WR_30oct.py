# program for reading and writing the data from excel file


import xlrd
import xlsxwriter

workbook = xlrd.open_workbook('dataxls7.xls')
worksheet = workbook.sheet_by_name('renu111')
totalrows = worksheet.nrows
totalcoloumns = worksheet.ncols
print("total rows", totalrows)
print("total cols:", totalcoloumns)
# code to create new excel file with the name resiltsfor2.xlsx
workbook1 = xlsxwriter.Workbook('32thresults.xls')
# adding the sheet to work book and shete name as results sheet
worksheet1 = workbook1.add_worksheet("Resultssheet")

passcount = 0
passcount = int(passcount)
failcount = 0
failcount = int(failcount)
parcialcount = 0
parcialcount = int(parcialcount)
# dict_list = []
# reading the data from input excel file
worksheet1.write(0, totalcoloumns, 'Totalpasscount')  # adding the header name as Passcount
worksheet1.write(0, totalcoloumns + 1, 'TotalFailcount')  # adding the header name as Failcount
worksheet1.write(0, totalcoloumns + 2, 'Parcialcount')  # adding the header name as Parcialcount
for row_index in range(-1, totalrows):
    # print("ros")
    for col_index in range(0, totalcoloumns):
        worksheet1.write(row_index, col_index, worksheet.cell(row_index, col_index).value)
        if ( col_index == 2 ):
            if ( worksheet.cell(row_index, col_index).value == 'Passed' ):
                passcount += 1
            elif(worksheet.cell(row_index, col_index).value == 'Failed'):
                failcount+=1
            else:
                parcialcount+=1

worksheet1.write(1, totalcoloumns, passcount)
worksheet1.write(1, totalcoloumns + 1, failcount)
worksheet1.write(1, totalcoloumns + 2, parcialcount)
workbook1.close()
# print(dict_list)
print("finally Done!Results for xls file is created with values")

