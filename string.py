import re

class regular_expression:
    string = input("Enter the string\n")

    catcount = len(re.findall("cat", string))
    dogcount = len(re.findall("dog", string))

    if catcount == dogcount:
        print(True)
    else:
        print(False)

class string_formatting:
    price = 40
    temp = "Price of the item is Rs. {}"
    print(temp.format(price))

class multiple_formatting(string_formatting):
    quantity = 3
    itemno = 567
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    #for extending methods use super(), for extending objects use classname
    print(myorder.format(quantity, itemno, string_formatting.price))