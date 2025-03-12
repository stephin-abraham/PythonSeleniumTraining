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
list2 = [1, 5, 7, 9, 3,1,2,1]
print(list2)
list3 = [True, False, False]
print(list3)
print(type(list3))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.