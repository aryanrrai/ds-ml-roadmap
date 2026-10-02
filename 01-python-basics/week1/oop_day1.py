class Dog:
    species = "Canis familiaris"      # class attribute: shared by all dogs

    def __init__(self, name, age):
        self.name = name              # instance attributes: unique per dog
        self.age = age

    def bark(self):                   # instance method
        return f"{self.name} says woof"

    def birthday(self):
        self.age += 1


bruno = Dog("Bruno", 3)
print(bruno.bark())        # Bruno says woof
bruno.birthday()
print(bruno.age)           # 4
print(Dog.species)         # shared value, reachable from the class


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def topper_subject(self):
        return max(self.marks, key=self.marks.get)


s1 = Student("Aryan", 101)
print(s1.name)
print(s1.roll_no)
print(s1.marks)
s1.add_marks("maths", 82)
s1.add_marks("science", 91)
print(s1.marks)
print(s1.average())
print(s1.topper_subject())