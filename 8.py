# WAP to take integer value from the user, keep asking for integer value, using an infinite loop, untill user enter a proper integer. if user enter a string, keep asking for integer value using infinite loop


while True:
 try:
    integer=int(input('kindly add an value'))
 except:
    
        print('add an valid value')
 else:
    print('value taken succesfully')
    break       

       

            