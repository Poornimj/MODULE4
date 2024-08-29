correctUsername = "python"
correctPassword ="rules"

attempts = 0
maxAttempts = 5
remainingAttempts = 5

while attempts < maxAttempts:
    userName = input("Enter your user name:")
    password = input("Enter your password:")

    if userName == correctUsername and password == correctPassword:
        print("Welcome!")
        break
    else:
        attempts += 1
        if remainingAttempts > 0:
            print(f"Incorrect user name or password. You have {remainingAttempts -1} attempts left.\n")
            remainingAttempts = remainingAttempts -1
        else:
            print("Access Denied.")