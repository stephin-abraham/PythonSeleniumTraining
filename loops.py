a,b=21,25
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
print("Condition over")
print("**********************************************")
Str="STephin Philip"
if Str == "Stephin Philip":
    print("Matches with the string")
else:
    print("Not matched")

#for loop
val1=[2,13,9.5,11,45,23]
for i in val1:
    print(i*2)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

#sum of first natural numbers-> 1+2+3+4+5 =15
#range(i,j) -> i to j-1
summation =0
for j in range(1,6):
    summation=summation+j
print(summation)

print("***********************************")
#printing values after jumping 2 values in loop
for k in range(1,10,2):        #here  loop works from 1 to 9 and skips 2 numbers using range(1,10,2)
    print(k)
