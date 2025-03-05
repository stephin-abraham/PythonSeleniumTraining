file = open('demo.txt')
# with open('demo.txt','r') as file:
# print(file.read())
# print(file.read(3))
# print(file.read(1))

# #print line by line using readLine method
# line=file.readline()
# while line != " ":
#     print(line)

print(file.readlines())

#if you want to open and close the file in one line then use
# syntax:-> with open('demo.txt') as file:
