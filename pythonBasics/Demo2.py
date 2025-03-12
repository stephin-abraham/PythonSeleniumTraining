#Mutable ->List is mutable that can be edited

values=[3,7.28,1,56,"Stephin"]
#printing last value by -1
print(values[-1])
print(values[1])
print(values[1:5])

#add value to the particular index
values.insert(3,"Philip")
print(values)

#add value to the end
values.append("Abraham")
print(values)

#remove value from the list
values.remove(1)
print(values)

#you can update the existing value
values[5]="STEPHIN"
print(values[5])

#deleting the index value
del values[3]
print(values)
