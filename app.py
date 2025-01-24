 class Student(object)
   Student_count = 0
   def _new_(self):
     print("Student._new_")

   def _init_(self):
     print("Student._init_")
     self.gpa = 4.00

   def study_hard(self):
     print("sir, yes sir.")
