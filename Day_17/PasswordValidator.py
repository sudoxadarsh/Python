# WAP user create a password length of minimum 8 and max any, first which contains
# alpha-numeric and special character combination....
# WAP take a full name as input and ensure password does not contain name or any subname.

special_chars = "!@#$%^&*()_+-=[]{};':,./<>?`~|\\\""

full_name = input("Enter full name: ").strip().lower().replace(" ", "")

while True:
    pass_word = input("Create password: ")
    password_lower = pass_word.lower()

    if len(pass_word) < 8:
        print("Password must be at least 8 characters long.")
    elif not pass_word[0].isalpha() or not pass_word[0].isupper():
        print("First character must be an uppercase alphabet.")
    elif not any(ch.isalpha() for ch in pass_word):
        print("Password must contain at least one letter.")
    elif not any(ch.isdigit() for ch in pass_word):
        print("Password must contain at least one number.")
    elif not any(ch in special_chars for ch in pass_word):
        print("Password must contain at least one special character.")
    else:
        contains_name_part = False
        for i in range(len(full_name)):
            for j in range(i + 2, len(full_name) + 1):
                part = full_name[i:j]
                if password_lower.find(part) != -1:
                    contains_name_part = True
                    break
            if contains_name_part:
                break

        if contains_name_part:
            print("Password must not contain your full name or any part of it.")
        else:
            print("Password is valid.")
            break

    print("Please try again.")

