class Person:
    def __init__(self, person_name: str, date_of_birth: int,
                 height: float = None, weight: int = None):
        self.__name = person_name
        self.__date_of_birth = date_of_birth
        self.__height = height
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_summary(self):
        return f"Name: {self.__name}, Date of Birth: {self.__date_of_birth}, " \
               f"Height: {self.__height if self.__height is not None else 'Not Given'}"


persons = [Person("Sayed", 1995, 5.65, 58),
           Person("Nur", 1990),
           Person("Saad", 2001, 5.9, 65),
           Person("Masum", 1985, 5.80, 78),
           Person("Sadia", 1990, 5.3, 52)]

for person in persons:
    if person.get_date_of_birth() is not None and person.get_date_of_birth() <= 1999:
        print(person.get_summary())


class Student(Person):
    def __init__(self, person_name: str, date_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name, date_of_birth)
        self.email_id = email_id
        self.student_id = student_id

    def get_summary(self):
        return f"Name: {self.get_name()}, Student Id: {self.student_id}, Email: {self.email_id}"


student = Student("Sayed", 1995, "nuruddinsayeed@gmail.com", "1537CSE00415")
print(student.get_summary())
