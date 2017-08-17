import re

timestamp = "Wednesday 3 May 2017, 1:57pm"
matchObj = re.search(r'(\w{3} \d{4},.+)', timestamp, re.M | re.I)
if matchObj:
    timestamp = matchObj.group(0)
    print("timestamp : ", timestamp)

else:
    print("No match!!")



