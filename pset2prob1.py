for i in range (12):
 minMonthlyPayment=balance*monthlyPaymentRate
 unpaid=balance-minMonthlyPayment
 interest=unpaid*annualInterestRate/12
 balance=interest+unpaid

print("Remaining balance: "+str(round(balance,2)))