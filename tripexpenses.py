
# Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip

hotelcost = 100 #2100 + 1200 +650
hoteldays = int(input("How many days are you staying? "))
hotelcost = hoteldays * hotelcost
plane = input("Which airline are you taking (q for Quatar, j for Jet airways or b for British airline)? ").upper()
if plane == "Q":
    planecost = 1500
elif plane == "J":
    planecost = 1200
elif plane== "B":
    planecost = 1000
else:
    print("You have entered something wrong.")
hoursrent = int(input("How many hours did you rent the vehicle? "))
vehiclecost = hoursrent * 50
vat = (hotelcost + planecost + vehiclecost) * 20/100
totalcost = hotelcost + planecost + vehiclecost + vat
print("The total cost is £{0}.".format(totalcost))