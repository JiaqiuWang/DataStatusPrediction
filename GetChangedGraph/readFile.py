
fo = open("G2.txt", "r+")
str = fo.read()
print("str:", str)
position = fo.tell()
print("postion:", position)

fo.close()
