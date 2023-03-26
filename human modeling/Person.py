class Person():
    def __init__(self, name, surname, age, place_of_birth):
        self.name = name
        self.surname = surname
        self.age = age
        self.place_of_birth = place_of_birth

    def info_about_yourself(self):
        print(f"My name is {self.name}.")
        print(f"My surname is {self.surname}.")
        print(f"I am {self.age} years old.")
        print(f"I was born in {self.place_of_birth}.")

    def age_person(self):
        self.age += 1
        print(f"My next birthday will be {self.age} years old.")

class Student(Person):
    def __init__(self, name, surname, age, place_of_birth, school, year_of_release, diploma_color, specialization):
        super(). __init__(name, surname, age, place_of_birth)
        self.school = school
        self.year_of_release = year_of_release
        self.diploma_color = diploma_color
        self.specialization = specialization

    def info_about_student(self):
        print(f"I studied at {self.school}.")
        print(f"Year of graduation {self.year_of_release}.")
        print(f"My diploma is {self.diploma_color}.")
        print(f"My specialization {self.specialization}.")

