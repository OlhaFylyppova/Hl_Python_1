# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача. Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human: {self.first_name} {self.last_name} gender {self.gender} age {self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {super().__str__()}, record_book {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        try:
            if len(self.group) == 10:
                raise CustomException("* This is a custom exception *", f"There are {len(self.group)} "
                                      f"students in the group. It is not possible to give more than 10 students. \n*** "
                                      f"No data about the student {student.first_name} {student.last_name} has been added ***")
        except CustomException as ms:
            print(ms.message)
            print(ms.val)
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student_find = self.find_student(last_name)
        if student_find:
            self.group.remove(student_find)

    def find_student(self, last_name):
        group_tuple = tuple(self.group)
        for param in range(len(group_tuple)):
            if last_name == group_tuple[param].last_name:
                return group_tuple[param]

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"\n{student}"
        return f'Number:{self.number}\\n {all_students} '

class CustomException(Exception):

    def __init__(self, message, val):
        super().__init__()
        self.message = message
        self.val = val

    def get_exception_message(self):
        return self.message


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
