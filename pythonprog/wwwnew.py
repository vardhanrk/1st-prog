import xlrd
import xlsxwriter
workbook = xlrd.open_workbook('dataxls7.xls')
worksheet = workbook.sheet_by_name('renu111')
totalrows = worksheet.nrows
totalcoloumns = worksheet.ncols
print("total rows", totalrows)
print("total cols:", totalcoloumns)
workbook1 = xlsxwriter.Workbook('vardhantestreports.xlsx')
worksheet1 = workbook1.add_worksheet()
#code to create new excel file with the name resiltsfor2.xlsx
passcount = 0
passcount = int(passcount)
failcount = 0
failcount = int(failcount)

for row_index in range(-1, totalrows):
    # print("ros")
        for col_index in range(-1, totalcoloumns):
		        #worksheet1.write(row_index,col_index,worksheet.cell(row_index, col_index).value)
	                 #worksheet1.write('D1', 'Totalpasscount')
				     print(worksheet.cell(row_index, col_index).value) 
     
				   
   # dict_list.append(d)

print("Total passcopunt", passcount)
print("Total failcount", failcount)
print("finally Done!Results for xls file is created with values")
workbook1.close()