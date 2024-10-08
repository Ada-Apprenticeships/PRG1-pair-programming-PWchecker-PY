import datetime
import re  

OUTPUT_FILE = "./checking_password_log.txt"


def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def read_in_file(filename):
    with open(filename, "r") as f:
            return f.read()
    

PASSWORD_CRITERIA = {
    "length": re.compile(r".{8,}"),  # Minimum 8 characters
    "uppercase": re.compile(r"[A-Z]"),  # Must have uppercase letters
    "lowercase": re.compile(r"[a-z]"),  # Must have lowercase letters
    "digit": re.compile(r"[0-9]"),  # Must have digits
    "special_char": re.compile(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/\|=]"),  # Must have special characters
}


def is_strong_password(password):
    for criteria in PASSWORD_CRITERIA.values():
        if not criteria.search(password):  
            return False
    return True


def get_password_strength(password):
    conditions_passed = 0
    for criteria in PASSWORD_CRITERIA.values():
        if criteria.search(password):  
            conditions_passed += 1

    if conditions_passed == 5:
        return "Strong"
    elif conditions_passed >= 3:
        return "Medium"
    else:
        return "Weak"


def get_password_from_user():
    while True:  # Loop until a strong password is entered
        password = input("Please enter your password: ")

        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{get_current_datetime_formatted()}\n")

        strength = get_password_strength(password)
        print(f"Password strength: {strength}")

        if strength == "Strong":
            print("Your password is strong.")
            break
        else:
            print("Password does not meet the criteria. Please enter a different password.")


# Read in the poor passwords (replace with actual implementation)
poor_passwords = read_in_file(OUTPUT_FILE)

# Main execution
get_password_from_user()