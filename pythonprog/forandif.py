# program for if numer 7 greater than should not print


nb = input('Choose a number: ')
# converting nb in to integer using int(nb)


i = int(nb)
for x in range(0, i):
    if ( x >= 7 ): break
    else : print ("We're on time %d" % x)
print ("Finallly ")
    