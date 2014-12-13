# program for creating the sample class passing the args to methods

class Vardhan:
      count=0 
      def __init__(self, name, age):
          self.name = name
          self.age = age
          Vardhan.count += 1

      def diplayname(self):
       print("This is his name", self.name)
  
      def displaytotaldetails(self):
       print("Total details :", self.name, ", age", self.age)


emp1 = Vardhan("Renu", 20)
emp1.diplayname()
emp1.displaytotaldetails()
