
inches_to_cm = 2.54

while True:

    inches = float(input("Enter a value in inches (negative value to quit): "))

    if inches < 0:
        print("Negative value entered. Program will now exit.")
        break

    centimeters = inches * inches_to_cm

    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.\n")