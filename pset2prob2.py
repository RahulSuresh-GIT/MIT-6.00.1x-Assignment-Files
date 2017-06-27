fixedMonthlyPayment = 10
temp = balance

while balance>0:
 for i in range (12):
     unpaid=balance-fixedMonthlyPayment
     interest=unpaid*annualInterestRate/12
     balance=interest+unpaid
    
 if balance<=0:
    break
 else:
   fixedMonthlyPayment+=10
   balance=temp

print("Lowest Payment: "+str(fixedMonthlyPayment))
   