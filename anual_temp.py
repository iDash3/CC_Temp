# \d{4,4}\s{1,}[\d]+\s{1,}[-\d.*]+\s{1,}[-\d.*]+              Regex for data
# (\d{4,4})\s{1,}([\d]+)\s{1,}([-\d.*]+)\s{1,}([-\d.*]+)      Regex with indent
# (\d{4,4})\s{1,}([\d]+)\s{1,}([-\d.*]+)\s{1,}([-\d.*]+).*    Whole sentence
# \s+(\d{4,4})\s{1,}([\d]+)\s{1,}([-\d.*]+)\s{1,}([-\d.*]+)   Regex for re module

import re
from collections import defaultdict
from decimal import Decimal

pattern = re.compile(r'\s+(\d{4,4})\s{1,}([\d]+)\s{1,}([-\d.]+)[*]?\s{1,}([-\d.]+)[*]?')

filename = 'Ballypatrick_Forest'
print('El archivo seleccionado es: {}'.format(filename))

f = open("docs/" + filename + ".txt", 'r')
f1 = open("res/" + filename + ".csv", "w+")
prev_year = ''
year_avg = defaultdict(list)
temp_years = []

global c
c = 0
c_limit = 70

for line in f:
	res = re.match(pattern, line)

	if res:
		temp_year = res.group(1)
		temp_month = res.group(2)
		# if res.group(3) and res.group(4) == '0':
		# 	print('Error')
		# 	temp_max = 0
		# 	temp_min = 0
		# 	temp_avg = 0
		# else:
		temp_max = float(res.group(3))
		temp_min = float(res.group(4))
		temp_avg = (temp_max+temp_min)/2

		if prev_year == temp_year:
			year_avg[int(c)].append(temp_avg)
		else:
			if c == c_limit:
				break
			c = c + 1 
			year_avg[int(c)].append(temp_avg)
			temp_years.append(temp_year)

		# op = '{},{},{},{}'.format(temp_year,temp_month,temp_max,temp_min)
		# op = '{}'.format(temp_year)
		# print("%s\n" % op)
		# f1.write(op + "\n")
		prev_year = temp_year

	else:
		print('Fail')


for k in range(len(temp_years)):
	year_sum = Decimal(sum(year_avg[k])/12)
	sum_op = round(year_sum,2)
	op = '{},{}'.format(temp_years[k],sum_op)
	f1.write(op + "\n")
	print(op)

f.close()
f1.close()