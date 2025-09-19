from student import Student
from librarian import Librarian
from software_dev import SoftwareDeveloper


class FileD:
    def __init__(self, path="students.txt"):
        self.path = path


    def read_file(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return [line.rstrip("\n") for line in f]
        except FileNotFoundError:
            return []

    def write_objects(self, objects):

        with open(self.path, "a", encoding="utf-8") as f:
            for obj in objects:
                if isinstance(obj, Student):
                    f.write(f"Student {obj.first_name} {obj.last_name}\n")
                    f.write("{\n")
                    f.write(f' "firstname": "{obj.first_name}",\n')
                    f.write(f' "lastname": "{obj.last_name}",\n')
                    f.write(f' "studentId": "{obj.student_id}"\n')
                    f.write(f' "passport":"{obj.passport}"\n')
                    f.write(f' "weight": "{obj.weight}",\n')
                    f.write(f' "height": "{obj.height}",\n')
                    f.write(" };\n\n")
                elif isinstance(obj, Librarian):
                    f.write(f"Librarian {obj.first_name}{obj.last_name}\n")
                    f.write("{\n")
                    f.write(f' "firstname": "{obj.first_name}",\n')
                    f.write(f' "lastname": "{obj.last_name}",\n')
                    f.write(f' "riding_bike": "{obj.ride_bike()}"\n')
                    f.write(" };\n\n")
                elif isinstance(obj, SoftwareDeveloper):
                    f.write(f"SoftwareDeveloper {obj.first_name}{obj.last_name}\n")
                    f.write("{\n")
                    f.write(f' "firstname": "{obj.first_name}",\n')
                    f.write(f' "lastname": "{obj.last_name}",\n')
                    f.write(f' "riding_bike": "{obj.ride_bike()}"\n')
                    f.write(" };\n\n")