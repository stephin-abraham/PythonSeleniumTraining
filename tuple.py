#tuple is immutable in nature and has to be initialized in () instead of []
value=(1,3.2,1.34,"Stephin")
print(value)

    #you cannot edit the existing values
# value[3]="STEPHIN"
# print(value)

#Dictionary initialization
dic={"a":2,6:"Stephin","b":"Sam"}
print(dic)

#if u want to print string var then u have to use " "
print(dic["b"])
print(dic[6])

#adding values to an empty dictionary
dict={}    #empty dict
dict["firstname"]="Stephin"
dict["lastname"]="Abraham"
dict["age"]=25
dict["gender"]="Male"

print(dict)
print(dict["lastname"])
