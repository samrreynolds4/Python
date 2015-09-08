class test(object):
    num = 0
    def _init_(self):
        print("created")
    def talk(self):
        print("talking")

number = test()

number.talk()
print(number.num)
number.num = 10
print(number.num)
