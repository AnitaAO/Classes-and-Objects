# Name: A string, should be initialized when creating an instance of Student
#  Age: An integer, should be initialized when creating an instance of Student
# Tracks: A list of strings, should be initialized when creating an instance of Student. Feel free to pick any values as tracks.
#  Score: A float, should be initialized when creating an instance of Student.    
# 3.  Create the following methods for class “Student”:

# change_name: Change students name, should accept a new name as an argument.
# Change_age: Change students' age, should accept a new age as an argument. Should ensure age remains an integer.
# Add_track: Add a new item to students tracks, should accept a new track as an argument.
# get_score: Return student’s score.

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self):
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()