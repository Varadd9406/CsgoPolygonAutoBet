def findNumberFromString(s):
	num = ''
	for i in s:
		if 48 <= ord(i) <= 57:
			num += i
	return int(num)
