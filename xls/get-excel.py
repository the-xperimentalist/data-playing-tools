import xlrd
book = xlrd.open_workbook('SOWC_2014_Stat Tables_Table 9.xlsx')

sheet = book.sheet_by_name('Table 9 ')

# print (sheet)
# print (dir(sheet))
# print (sheet.nrows)

data = {}

for i in range(14, sheet.nrows):

	row = sheet.row_values(i)

	country = row[1]

	data[country] = {
	'child_labor': {
	'total': [row[4], row[5]],
	'male': [row[6], row[7]],
	'female': [row[8], row[9]],
	},
	'child_marriage': {
	'married_by_15': [row[10], row[11]],
	'married_by_18': [row[12], row[13]]
	}
	}

	if country == 'Zimbabwe':
		break

import pprint
pprint.pprint(data)
