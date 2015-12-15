class SchoolMember:
    #any man in school
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(School member {0} created)'.format(self.name))

    def tell(self):
        #show info
        print('Name: "{0}", age: {1}'.format(self.name, self.age),end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salery = salary
        print('(Teacher created: {0})'.format(self.name))

    def tell(self):
        print('Salary: "{0:d}"'.format(self.salery))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Student {0} created)'.format(self.name))

    def tell(self):
        print('Marks {0}'.format(self.marks))

t = Teacher('Mr. Borya', 40, 12000)
s = Student('John', 13, 75)

print()

members = [t,s]
for member in members:
    member.tell()

