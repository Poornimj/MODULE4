numbers = []

while True:
    userInput = input("Enter a number (or press Enter to quit):")

    if userInput =="":
        break

    try:
        number = float(userInput)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"The smallest number entered is: {smallest}")
        print(f"The largest number entered is: {largest}")
else:
    print("No numbers were entered.")


