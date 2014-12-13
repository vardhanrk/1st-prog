#writing the program using functions 


def category( a, b, c):
    b=int(b)
    if ( b <= 22): print("He is adult")
    else: print("He is uncle") 
    print ( a, b, c)


name= input('Write a name: ')
age= input('Write u r  Age: ')
dept= input('Write u r  Depart ')

category( name, age, dept );