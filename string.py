import re

string = input("Enetr the string")

catcount = len(re.findall("cat", string))
dogcount = len(re.findall("dog", string))

if catcount == dogcount:
    print(True)
else:
    print(False)
