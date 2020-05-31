import os

file = open('demo.txt', "a")
file.write("\nHello World.\nIt's a new day")
file.close()

file_read = open('demo.txt', 'r')
for i in file_read:
    print(i)
print(file_read.read())
file_read.close()

class file_removal:
    if os.path.exists('demo.txt'):
        print('File exist')
        os.remove('demo.txt')
        print('File deleted')
    else:
        print("File doesn't exist")
