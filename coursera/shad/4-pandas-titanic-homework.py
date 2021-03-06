#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
		Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
Какую долю пассажиры первого класса составляли среди всех пассажиров?
		Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
		В качестве ответа приведите два числа через пробел.
Коррелируют ли число братьев/сестер с числом родителей/детей?
		Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
Какое самое популярное женское имя на корабле?
		Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
		Это задание — типичный пример того, с чем сталкивается специалист по анализу данных.
		Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию
		Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для
		извлечения имен, а также разделения их на женские и мужские.
Если ответом является нецелое число, то целую и дробную часть необходимо разграничивать точкой, например, 0.42.
		При необходимости округляйте дробную часть до двух знаков.

Ответ на каждое задание — текстовый файл, содержащий ответ в первой строчке.
		Обратите внимание, что отправляемые файлы не должны содержать пустую строку в конце.
		Данный нюанс является ограничением платформы Coursera. Мы работаем над тем, чтобы убрать это ограничение.
"""

import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# -> males, females
print data['Sex'].value_counts()


print data['Survived'].value_counts()