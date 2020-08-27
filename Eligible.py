#A PROGRAM THAT HAS CLASS PERSON STORING NAME AND DOB OF PERSON. PROGRAM NEED TO SUBTRACT DOB FROM CUREENT DATE TO CHECK IF PERSON IS ELIGIBLE TO VOTE. 
import datetime
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    def eligible(self):
        if(person.age() > 18):
            print("Eligible to Vote")
        else:
            print("Not Eligible to Vote")
person = Person("Ayush",datetime.date(1998, 12, 5))
print(person.name)
print(person.age())
person.eligible()
