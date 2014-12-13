# program for  inheritence concepts




class Parent:
      def __init__(self):
          print("calling the parent constructor")

      def parentmethod(self):
          print(" calling the parent nethod ")


class chaild(Parent):
      def __init__(self):
          print("calling the chaild cons")
      def chaildmethod(self):
          print("calling the chaild method")


c=chaild()
c.parentmethod()
c.chaildmethod()