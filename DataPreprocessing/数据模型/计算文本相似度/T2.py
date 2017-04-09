import Levenshtein
str1 = "@klausbyskov: This is not true. Entity Framework / LINQ to Entities is unable to do this in .NET 3.5, but LINQ to SQL will be happy to convert this into SQL. The only gotcha is that the number of elements in the IN( ) clause (the number of elements in the &#39;name&#39; list) is limited, due to limitations of ADO.NET."
str2 = ""

a = Levenshtein.ratio('asdf', 'sd4fa4')

print("a:", a)

b = Levenshtein.distance('asdf', 'asdo98')
print("b:", b)
