from logging import exception

itemCart = 0

if itemCart != 2:
    pass
assert(itemCart == 0)

try:
    with open('file1.txt','r') as reader:
        reader.read()
    # if itemCart == 2:
    #     print("nothing")
    # else:
    #     print("yes")
except:
    print("No such file is present in the directory")
