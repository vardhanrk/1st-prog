# program for reading the data from text file and writeing the data in to test file with spitting data in to spaces



import os 


fo = open("textread.txt", "r+")
str = fo.read();
print ("Read String is : ", str)

frs = str.split(",")

for fr in frs:
    print("s",fr)

# Close opend file
fo.close()

