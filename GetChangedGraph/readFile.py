
fo = open("G3.txt", "r+")
str = fo.read()
print("str:", str)
position = fo.tell()
print("postion:", position)

fo.close()
