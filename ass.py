from os import system
a = (1, 2, 3,)


choices = ['aaa', 'bbbb', 'cccc']

acount=0
bcount=0
ccount=0
pas=4

for x in a :

 g=(int(input("enter pass")))
 z = int(input("enter your id"))
 if (g==pas):

   if z in a:
    print(choices)
    y=input("enter your choice")
    system('cls')
    if (y==choices[0]):
        acount=acount+1
    elif (y==choices[1]):
        bcount=bcount+1
    elif (y==choices[2]):
        ccount=ccount+1
    else:
        print("wrong info ")
        system('cls')


   else:
    print("you are not eligible to vote")
    system('cls')



 else:
    print("wrong password")
    system('cls')
if acount>bcount and acount>ccount:
    print (choices[0]+" has won the elections")
elif bcount>acount and bcount>ccount:
    print (choices[1]+" has won the elections")
elif ccount>acount and ccount>bcount:
    print (choices[2]+"has won the election")
else:
    print ("there has been a draw")





print("number of votes a has:",acount)
print("number of votes b has:",bcount)
print("number of votes c has:",ccount)