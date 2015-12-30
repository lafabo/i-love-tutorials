string = str(raw_input("Enter the string, please: ")).split()

longest = ''
for i in string:
	if len(i) > len(longest):
		longest = i

print longest
