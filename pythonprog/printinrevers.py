# program for read thge data from test 1 and paste in to test2.txt in reverse order



import os 


fo = open("text1.txt", "r+")
str = fo.read();
splitdata=str.split(" ");
# print(splitdata[2])
 
s=1
onetoten = range(0,len(splitdata))



count = 0
allcount= len(splitdata)
print(allcount)
while (count < allcount):
   print ('The count is:',count, splitdata[count])
   count = count+1


fo1 = open("text2.txt", "w")
os.path.exists("dir/text2.txt")


while (allcount > 0):
   allcount = allcount-1
   data=splitdata[allcount]
  # fo1.write(splitdata[allcount],"%d")
   fo1.write(data)
   print ('The count is:', allcount, splitdata[allcount])

   # print ('The count is:', splitdata[allcount-1])
   


# for count in onetoten:
   
   # print(splitdata[count])


# print ("Read String is : ", str)
# Close opend file
