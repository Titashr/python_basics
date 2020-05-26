print("Palindrome Test\n")

string1 = input("Enter the string to test")


def palindrome(input1):
    stringnew = input1[::-1]
    if stringnew == input1:
        print(True)
    else:
        print(False)


palindrome(string1)
