def is_power(a, b):
	if a % b == 0 and is_power(a/b, b) == 0:
		return True
	else:
		return False

print is_power(9, 3)
print is_power(2, 15)
print is_power(64, 2)
print is_power(1, 1)

# todo this script don't work!