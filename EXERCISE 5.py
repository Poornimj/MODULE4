correct_username = "python"
correct_password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect username or password. You have {remaining_attempts} attempts left.\n")
        else:
            print("Access denied.")