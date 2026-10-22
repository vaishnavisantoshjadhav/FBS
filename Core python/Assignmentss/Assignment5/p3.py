#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n = int(input('Enter the number of passenger:'))
tcost = int(input('Enter the ticket cost per person:'))

total = 0

for i in range(n):
    age = int(input('Enter age of the person'))

    if age < 12 :
        amount = tcost * 70/100
    elif age > 59:
        amount = tcost * 50 / 100
    else:
        amount = tcost
        total += amount
print("Total amount=",total)    