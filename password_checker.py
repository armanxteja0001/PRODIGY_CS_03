import re

def check_password_strength(password):
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, upper_error, lower_error, digit_error, special_error]
    score = 5 - sum(errors)

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# === Interface ===
print("🔐 Password Strength Checker 🔐")
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
