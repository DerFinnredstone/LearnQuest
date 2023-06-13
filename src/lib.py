from ursina import *

class Calendar:
    def __init__(self):
        self.schedule = {}

    def add_event(self, date, event):
        if date in self.schedule:
            self.schedule[date].append(event)
        else:
            self.schedule[date] = [event]

    def get_events(self, date):
        if date in self.schedule:
            return self.schedule[date]
        else:
            return []

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0

        total = sum(self.grades.values())
        return total / len(self.grades)

class Chat:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, message):
        self.messages.append((sender, message))

    def get_messages(self):
        return self.messages

def start_command():
    command = "python f:/LearnQuest/src/main.py"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output.decode("utf-8"))