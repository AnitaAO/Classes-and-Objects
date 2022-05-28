# Name: A string, should be initialized when creating an instance of Student
#  Age: An integer, should be initialized when creating an instance of Student
# Tracks: A list of strings, should be initialized when creating an instance of Student. Feel free to pick any values as tracks.
#  Score: A float, should be initialized when creating an instance of Student.    
# 3.  Create the following methods for class “Student”:

# change_name: Change students name, should accept a new name as an argument.
# Change_age: Change students' age, should accept a new age as an argument. Should ensure age remains an integer.
# Add_track: Add a new item to students tracks, should accept a new track as an argument.
# get_score: Return student’s score.
from unicodedata import name


class Student:

    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, track, score):

        self.student_name = name
        self.student_age = age
        self.student_track = track
        self.student_score = score

Anita = Student('name', 'age', 'track', 'score')
Amarachi = Student('name', 'age', 'track', 'score')
Anita.name = "Anita"
Anita.age = 32
Anita.track = ["FE", "BE"]
Anita.score = 20.50

Amarachi.name = "Amarachi"
Amarachi.age = 36
Amarachi.track = ["UI/UX", "FE"]
Amarachi.score = 50.20
print(Amarachi.name)
print(Anita.age)

# methods
def change_name(self, name):
    self.change_name = name
    print(Anita, self.name)

def change_age(self, age):
    self.change_age = age
    print(32, self.age)

def add_track(self, track):
    self.self.append(track)
    print("BE", self.track)

def get_score(self):
    print(f"The score remains {self.score}")
