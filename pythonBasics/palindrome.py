class palindrome:
    n=701
    rev=0
    originalnum = n
    while n != 0:
        rem=n%10
        rev=rev*10 + rem
        n= n//10

    if originalnum == rev:
            print(str(rev) + " It is a palindrome")
    else:
        print("original number is "+str(originalnum)+" and "+str(rev) +" Not a palindrome")




