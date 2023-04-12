room_type = input("Enter type of room booked (Deluxe/Non AC): ")
days = int(input("Enter total number of days: "))
food_amount = float(input("Enter total amount on food: "))

# calculate room tariff
if room_type.lower() == "deluxe":
    room_tariff = 7500 * days
elif room_type.lower() == "non ac":
    room_tariff = 4500 * days
else:
    print("Invalid room type entered.")
    exit()

# calculate tax on food amount
if room_type.lower() == "deluxe":
    cgst = round(0.09 * food_amount, 2)
    sgst = round(0.09 * food_amount, 2)
    tax = cgst + sgst
elif room_type.lower() == "non ac":
    cgst = round(0.025 * food_amount, 2)
    sgst = round(0.025 * food_amount, 2)
    tax = cgst + sgst
else:
    print("Invalid room type entered.")
    exit()

# calculate tip amount and grand total
tip = round(0.1 * food_amount, 2)
grand_total = room_tariff + food_amount + tax + tip

# print bill
print("Room Tariff: INR {:.2f}".format(room_tariff))
print("GST on Food: CGST INR {:.2f}, SGST INR {:.2f}".format(cgst, sgst))
print("Tip: INR {:.2f}".format(tip))
print("Grand Total: INR {:.2f}".format(grand_total))