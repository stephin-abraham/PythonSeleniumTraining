# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
print("****************                Tuple built-in data types in Python *******************************")

thisTuple = ("dog","cat","dog","dog")
print(thisTuple)
# thisTuple[3] = "cat"
# print(thisTuple)
print("********************************")

# But, in Python, we are also allowed to extract the values back into variables.
# This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print("*************************************************")

thistuple = ("curry", "lebron", "kobe","kyrie","durant")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

print("*************************************************")
for i in range(len(thistuple)):
    print(thistuple[i])

print("****************                SET built-in data types in Python *******************************")
# A set is a collection which is unordered, unchangeable*, and unindexed.
thisSet = {1,2,"Stephin","Curry","Abraham"}
print(thisSet)

#                             unchangeable*
# thisSet[1] = True
# print(thisSet)

# no duplicates are allowed
thisSet2 = {1,1,45,7,1,67}
print(thisSet2)

# to add anew value use add()
thisSet2.add(89)
print(thisSet2)

print("*************************************************")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)