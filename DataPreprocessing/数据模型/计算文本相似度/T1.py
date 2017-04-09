import difflib as dlb

a = dlb.SequenceMatcher(None, 'abcde', 'abcde2').ratio()
print("ratio:", a)














