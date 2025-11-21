import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @staticmethod
    def read_json(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

        students = []
        for item in data["students"]:
            student = Student(item["name"], item["age"], item["grades"])
            students.append(student)

        return students

    def calc_average(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    @staticmethod
    def write_averages(students, output_file):
        result = {}
        for s in students:
            result[s.name] = s.calculate_average()

        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)


############################################################################################
students = Student.read_json("students.json")

Student.write_averages(students, "averages.json")

print("Done! File 'averages.json' created.")
