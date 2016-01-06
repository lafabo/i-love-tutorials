# -*- coding: utf-8 -*-

'''
Написать программу декодирования телефонного номера для АОН.
По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
— Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
— Каждая значащая цифра повторяется минимум 2 раза
— Если в номере идут несколько цифр подряд, то для обозначения
	«такая же цифра как предыдущая» используется идущий
	 2 или более подряд раз знак #

Например, входящая строка 4434###552222311333661 соответствует номеру 4452136
Кстати, регулярные выражения использовать в этих заданиях — нельзя :)
'''


string = str(raw_input('Phone number: '))

for i in len(string)+1:
	if string[i] == string[i - 1]:
		string = string[:i:]
		print string

print 'final ', string