#get details of the loan

money_owed = float(input('How much do you owe? '))
annual_interest = float(input('How much is your annual interest? '))
payment = float(input('How much are you paying per month? '))
month = int(input('How many months do you want to pay it? '))

#calculate the monthly rate
monthly_interest = annual_interest /100/12

for i in range(month):

    interest_paid = money_owed * monthly_interest

    money_owed = money_owed + interest_paid
    money_owed = money_owed - payment
    
    if(money_owed < 0):
        print('Debt settled')
    else:
         print('The last payment', money_owed)
         print('You paid of the loan in ', i + 1, ' months')
        
       
         break
    #make a payment
       

   