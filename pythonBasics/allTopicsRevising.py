print("Stephin Philip Abraham")
x,y= "Good Boy","Homely Guy"
age = 25
# concatinating the string and the integer using f-string
text = f"My age is {age}"
print(x +" "+ y+text)

z=int(7.8)
print(z)

q= int("8")
print(q)

a= "Stephin, Philip"
print(a[1])
print("********************************")
for b in a:
    print(b)
print("********************************")
print(a[2:5])

print("********************************")
print(a[:6])

print("********************************")
print(a.upper())
print(a.lower())

# List items are ordered, changeable, and allow duplicate values.
list = ["hello","all","world","all","hello"]
print(list)
print(type(list))
print("*************************************************")
list2 = [1, 5, 7, 9, 3,1,2,1]
list2.append(10)
print(list2)
print("*************************************************")
list3 = [True, False, False]
list3[1] = True
print(list3)
print("*************************************************")
print(type(list3))
print("*************************************************")
list.extend(list3)
print(list)
print("*************************************************")

for i in range(len(list3)):
    print(list3[i])
print("*************************************************")
# while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("*************************************************")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

print("*************************************************")
abc= ["dog","cat","lion","tiger"]
copy1 = abc.copy()
print(copy1)

copy1.reverse()
print(copy1)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.