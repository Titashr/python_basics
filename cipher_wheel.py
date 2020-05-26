print("Ceaser's cipher\n")

inputString = input("Enter the required string : ")
inShift = int(input("Enter the required string : "))


def my_cipher(string1, shift1):
    stringList = list(string1)
    length = len(stringList)
    result = ""
    for i in range(length):
        test=stringList[i]
        if test.islower():
            result +=chr((ord(test)+shift1-97) % 26 + 97)
        else:
            result += chr((ord(test) + shift1 - 65) % 26 + 65)
    return result


result = my_cipher(inputString, inShift)
print(result)
