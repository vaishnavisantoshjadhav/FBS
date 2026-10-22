#Find minimum number of notes required for an amount
amount = int(input("Enter amount: "))

notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

count = 0

for note in notes:
    number = amount // note

    if number > 0:
        print(note, ":", number)

    count = count + number
    amount = amount % note

print("Minimum number of notes/coins =", count)