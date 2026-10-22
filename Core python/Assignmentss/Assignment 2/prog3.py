#Convert distance given in feet and inches into meter and centimeter
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches

meters = total_inches * 0.0254
centimeters = meters * 100

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)