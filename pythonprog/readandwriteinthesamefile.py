# program for reading and writing the data from excel file


import xlrd
import xlsxwriter
# open the excel file
workbook = xlrd.open_workbook('dataxls5.xls')
worksheet = workbook.sheet_by_name('renu111')
totalrows=worksheet.nrows
totalcols=worksheet.ncols
print("totalrows :", totalrows, "Totalcols :", totalcols)
# creating the new sheet with name as "Results "

workbook1 = xlsxwriter.Workbook('dataxls5.xls')
worksheet1 = workbook1.add_worksheet('results') 



workbook1.close()
# print(dict_list)
print("finally Done!Results for xls file is created with values")
