# bank.py
# This program asks the user to input two amounts in cent and then prints out the sum of these in euro
# author: Niamh Hogan 

amount1 = int(input('Enter amount1 (in cent): '))
amount2 = int(input('Enter amount2 (in cent): '))
newAmount = float (amount1 + amount2)
print ("The sum of these is €" + str(newAmount/100))