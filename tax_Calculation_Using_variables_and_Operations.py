income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
lowtaxland_amt = income*lowtaxland_rate
ripoffland_amt = income*ripoffland_rate

# print("Your income is " + str(income) +" and you would pay " + str(lowtaxland_amt) + " income tax in Lowtaxland or " + str(ripoffland_amt)+ " income tax in Ripoffland. You would save " + str(ripoffland_amt - lowtaxland_amt) , "by paying taxes in Lowtaxland!")
#print("Your income is {} and you would pay {} income tax in Lowtaxland or {} income tax in Ripoffland. You would save {} by paying taxes in Lowtaxland!".format(income,lowtaxland_amt,ripoffland_amt,ripoffland_amt- lowtaxland_amt))
print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')