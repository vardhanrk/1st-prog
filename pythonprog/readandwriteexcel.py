# program for reading and writing the data from excel file


import xlrd
import xlsxwriter
workbook = xlrd.open_workbook('dataxls3.xls')
worksheet = workbook.sheet_by_name('renu')
totalrows = worksheet.nrows - 1
totalcoloumns= worksheet.ncols - 1
workbook1 = xlsxwriter.Workbook('results.xlsx')
worksheet1 = workbook1.add_worksheet('sheet1')

# print(totalcoloumns)
# print(totalrows)
curr_row = -1
while curr_row < totalrows:
	curr_row += 1
	row = worksheet.row(curr_row)
	print ('Row:', curr_row)
	curr_cell = -1
	while curr_cell < totalcoloumns:
		curr_cell += 1
		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
		cell_type = worksheet.cell_type(curr_row, curr_cell)
		cell_value = worksheet.cell_value(curr_row, curr_cell)
		# print (cell_value, cell_type)
                

worksheet1.write('A1', 'hello whts up')
# worksheet1.write('A2', curr_row)             
workbook1.close()

print("finally Done!")
