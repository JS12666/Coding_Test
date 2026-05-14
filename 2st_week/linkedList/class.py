class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("created", self.name, self)

    def talk(self):
        print("저는 ", self.name, "입니다")

person_1 = Person("이름1")
person_1.talk()

person_2 = Person("이름2")
person_1.talk()