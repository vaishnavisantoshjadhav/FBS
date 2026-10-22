"""11. Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full."""

age1 = int(input("Enter age of person 1: "))
ticket1 = int(input("Enter ticket amount: "))

age2 = int(input("Enter age of person 2: "))
ticket2 = int(input("Enter ticket amount: "))

age3 = int(input("Enter age of person 3: "))
ticket3 = int(input("Enter ticket amount: "))

age4 = int(input("Enter age of person 4: "))
ticket4 = int(input("Enter ticket amount: "))

age5 = int(input("Enter age of person 5: "))
ticket5 = int(input("Enter ticket amount: "))


if age1 < 12:
    ticket1 = ticket1 - (ticket1 * 30 / 100)
elif age1 > 59:
    ticket1 = ticket1 - (ticket1 * 50 / 100)

if age2 < 12:
    ticket2 = ticket2 - (ticket2 * 30 / 100)
elif age2 > 59:
    ticket2 = ticket2 - (ticket2 * 50 / 100)

if age3 < 12:
    ticket3 = ticket3 - (ticket3 * 30 / 100)
elif age3 > 59:
    ticket3 = ticket3 - (ticket3 * 50 / 100)

if age4 < 12:
    ticket4 = ticket4 - (ticket4 * 30 / 100)
elif age4 > 59:
    ticket4 = ticket4 - (ticket4 * 50 / 100)

if age5 < 12:
    ticket5 = ticket5 - (ticket5 * 30 / 100)
elif age5 > 59:
    ticket5 = ticket5 - (ticket5 * 50 / 100)


total = ticket1 + ticket2 + ticket3 + ticket4 + ticket5

print("Total ticket amount =", total)