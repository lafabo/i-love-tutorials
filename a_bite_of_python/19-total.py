# coding=utf-8
#переменное число параметров ._.
def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count+= number
    for key in keywords:
        count += keywords[key]

    return count


print(total(10, 1, 2, 3, vegetables=50, fruits=100))

'''
Когда мы объявляем параметр со звёздочкой (например,*param),
все позици-онные аргументы начиная с этой позиции и до конца
будут собраны в кортежпод именем param.

Аналогично, когда мы объявляем параметры с двумя звёздочками
(**param),все ключевые аргументы начиная с этой позиции и до
конца будут собраныв словарь под именем param
'''