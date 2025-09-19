from lab_1.librarian import Librarian
from lab_1.software_dev import SoftwareDeveloper
from lab_1.student import Student
from lab_1.file_manager import FileD

class ConsoleMenu:
    def __init__(self):
        self.fm = FileD()
        self.students = []

    def show_menu(self):
        while True:
            print("\n=== МЕНЮ ===")
            print("1. Додати особу")
            print("2. Показати всіх з файлу")
            print("3. Порахувати студентів з ідеальною вагою")
            print("4. Вихід")

            choice = input("Ваш вибір: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_all()
            elif choice == "3":
                self.count_students_with_ideal_weight()
            elif choice == "4":
                print("Вихід...")
                break
            else:
                print("Невірний вибір!")

    def add_student(self):
        choose=int(input("Кого хочете дододати 1. Student  2. Librarian 3. Developer?"))
        if choose==1:
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            student_id = input("Введіть ID студента: ")
            passport = input("Введіть паспорт студента: ")
            weight = int(input("Введіть вагу: "))
            height = int(input("Введіть зріст: "))
            s = Student(first_name, last_name, student_id, passport, weight, height)
            self.students.append(s)
            self.fm.write_objects([s])

        elif choose == 2:
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            l = Librarian(first_name, last_name)
            self.students.append(l)
            self.fm.write_objects([l])
        elif choose==3:
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            developer=SoftwareDeveloper(first_name,last_name)
            self.students.append(developer)
            self.fm.write_objects([developer])

        print("Особу додано!")

    def show_all(self):
        data = self.fm.read_file()
        if not data:
            print("Файл порожній.")
        else:
            print("\n".join(data))

    def count_students_with_ideal_weight(self):
        count = 0
        for s in self.students:
            if isinstance(s, Student) and s.is_ideal_weight():
                count += 1
        print(f"Кількість студентів з ідеальною вагою: {count}")