print 'The script is checking can or cannot exist triangle with such sides'
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


def is_triangle(a, b, c):
	if c > a + b or a > c + b or b > a + c:
		return 'No'
	else:
		return 'Yes'

print is_triangle(a, b, c)


