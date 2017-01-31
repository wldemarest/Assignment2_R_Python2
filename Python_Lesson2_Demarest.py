#W_Demarest 
#DS 710 Python Amoritization
 

loan_amt = float(input('Please enter principal loan amount: '))
int_rate = float(input('Please enter interest rate. For example if 5%  type .05: '))
month_pmt = float(input('Please enter monthly payment: '))
#Set interest amount & balance amount & step
mon_int_rate= int_rate / 12.0
balance=loan_amt
step=1
total_int=0


cannot_pay = 0

#Set column headers
print('%4s%10s%10s%8s' %('month','payment','interest','balance' ))
 
#loop will continue until balance=0
while balance>0:
#If balance exceeds loan amount stop loop

    old_balance = balance
    if balance > loan_amt:
        print('Error, Balance cannot exceed loan amount. Please try again')
        break


   
#If balance remaining is less than payment, use balance for payment
    elif balance <= month_pmt:
        interest = balance * mon_int_rate
        if(balance + interest < month_pmt):
            
            month_pmt = balance
            balance = 0
            print("%4d%10.2f%10.2f%10.2f" %(step,round(month_pmt,2),round(interest,2),round(balance,2)))
        else:   
            balance = balance - month_pmt + interest
            print("%4d%10.2f%10.2f%10.2f" %(step,round(month_pmt,2),round(interest,2),round(balance,2)))

        total_int += interest   
        step=step+1

    
        
    
#If balance left is greater than monthly payment, deduct monthly payment from balance
    else: 
        interest = balance * mon_int_rate
        balance = balance - month_pmt + interest

        print("%4d%10.2f%10.2f%10.2f" %(step,round(month_pmt,2),round(interest,2),round(balance,2)))
        total_int += interest
        
        step=step+1


    if balance > old_balance:
        print('Monthly payment too low. Balance can never be paid')
        cannot_pay = 1
        break        
#Calculate number of years and months required to pay balance & provide total payment amount               
#         else:        
#               print ('It's taken ', (step-1)//12, ' years and ', (step-1)%12, ' months to pay off the loan. Total payment is $', '%.2f'% round((loan_amt+total_int),2)) 



if(cannot_pay == 0):
    step = step - 1
    years = step /12
    monnths = step % 12

    print("It takes %d years and %d months to pay total amount" %(years,monnths))

    total_amt = total_int + loan_amt
    print('Total amount paid %.2f' %(round(total_amt,2)))