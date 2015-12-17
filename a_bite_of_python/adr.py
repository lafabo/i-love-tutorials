'''
Создайте собственную программу «Адресная книга»,
работающую из командной стро-ки и позволяющую
просматривать, добавлять, изменять, удалять или
искать контактныеданные ваших знакомых. Кроме того,
эта информация также должна сохраняться на дис-ке для
последующего доступа.Это достаточно простая задача,
если думать о ней в терминах, которые мы до сих порпроходили.
Если же вы всё-таки нуждаетесь в подсказке, как действовать
вот она.

Подсказка (не читать!)Создайте класс для хранения персональных данных.
Объекты визитных карточек храни-те в словаре, в котором имена контактов
будут служить ключами. Для длительного хра-нения этих объектов на
жёстком диске воспользуйтесь модулем pickle. Для добавления,
изменения или удаления контактов применяйте встроенные методы словаря.
'''

import pickle, os, argparse

class Adress:
    #any man in book
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment
        print('(Member {0} created)'.format(self.name))

parser = argparse.ArgumentParser(description="PhoneBook")
parser.add_argument('-a', help='add new')
parser.add_argument('-r', help='remove')
parser.add_argument('-f', help='find')
parser.add_argument('-e', help='edit')
args = parser.parse_args()


def viewall():
    pass

def addnew(name, phone, *comment):
    n = Adress;
    n.name = args.r
    n.phone = args.r

def remove(name):
    pass