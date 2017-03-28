import re

str1 = "asdf5463214563"
str2 = "asdfad4554"

matchObj = re.search(r'(\d{10})', str1, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group(0))
   # print ("matchObj.group(1) : ", matchObj.group(1))
   # # print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


