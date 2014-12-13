# program for reading the data from text file


import os 


fo = open("foo.txt", "r+")
str = fo.read();
print ("Read String is : ", str)
# Close opend file
fo.close()


fo1 = open("foo1.txt", "w")
os.path.exists("dir/foo1.txt")

fo1.write(str)