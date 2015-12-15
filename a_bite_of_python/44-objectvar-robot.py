class Robot:

    popolation = 0

    def __init__(self, name):
        self.name = name
        print("(Inicialization {0})".format(self.name))
        Robot.popolation += 1

    def __del__(self):
        print('{0} destroyng'.format(self.name))
        Robot.popolation -= 1

        if Robot.popolation == 0:
            print("{0} was last".format(self.name))
        else:
            print("Lasts {0:d} working robots".format(Robot.popolation))

    def sayhi(self):
        print("Hi! My masters call me {0}".format(self.name))

    def howmany():
        print("We have {0:d} robots".format(Robot.popolation))

    howmany = staticmethod(howmany)

droid1 = Robot('Pi')
droid1.sayhi()
Robot.howmany()

droid2 = Robot('wwZ')
droid2.sayhi()
Robot.howmany()

print("\nhere robots can work\n")
print('robots done for today. Let\'s destroy them')


