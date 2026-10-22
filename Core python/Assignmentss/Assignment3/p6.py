#Write a program to calculate profit or loss.

cp = int(input('Enter the cost price:'))
sp = int (input('Enter the selling price:'))
if sp > cp:
    profit = sp - cp
    print('there is profit',profit)
if sp < cp :
    loss = cp - sp
    print('There is a loss',loss) 
#cp - sp = loss
#sp - cp =profit