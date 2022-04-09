# making an e-mail validator that checks all the parameters of an input to be an email ID.

email = (input("Enter your Email ID :-"))

k,j,d=0,0,0

#Nested Conditions to check for various parameters
#Check For minimum len 7
if len(email)>=6:
    if email[0].isalpha(): #Checks for input alphabets
        if ('@' in email) and (email.count('@')==1):  #Checks for @ in email and checks for only single appearance of @
            if(email[-4]=='.') ^ (email[-3]=='.'): #XOR Operator(True if only one is true) Checks for . at -3 or -4 index
                for i in email: #iterating the string for various input search
                    if i == i.isspace(): #checks for space
                        k=1
                    elif i == i.isalpha(): #Checks for alphbet
                        if i == i.upper():
                            j=1
                    elif  i.isdigit():#Checks for digit
                        continue
                    elif i == "_" or i == "." or i == "@": #Checks for underscore , .dot and @.
                        continue
                    else:
                        d=1
                if k == 1 or j == 1 or d == 1:
                    print("Input Error- Space or isDigit or Uppercase or no Alpha")
            else:
                print("Input Error- Wrong Format/ No . in string")
        else:
            print("Input Error- Wrong Format/No @ in string")
    else:
        print("Input Error- Not Alphabet")
else:
    print("Input Error- Length less 6 or 6")

