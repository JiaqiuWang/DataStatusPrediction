import re

str1 = "Sun 03 02_ 2008"
str2 = "asdfad4554"

matchObj = re.search(r'(\d{1,2} \d{1,2}.*)', str1, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group(0))
   # print ("matchObj.group(1) : ", matchObj.group(1))
   # # print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


