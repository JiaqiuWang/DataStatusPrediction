import re

str1 = "Uploaded on Feb 24, 2011"
str2 = "asdfad4554"

matchObj = re.search(r'(\D{3} \d{1,2}, \d{4})', str1, re.M | re.I)

if matchObj:
    print("matchObj.group() :", matchObj.group(0))
   # print ("matchObj.group(1) : ", matchObj.group(1))
   # # print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


