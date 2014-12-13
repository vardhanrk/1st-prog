# program for reading the data from text file



fo = open("foo.txt", "r+")
str = fo.read();
print ("Read String is : ", str)
# Close opend file
fo.close()