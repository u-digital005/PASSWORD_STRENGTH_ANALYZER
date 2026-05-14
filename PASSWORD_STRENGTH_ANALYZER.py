import re
import random
import string

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


def suggest_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(14))


def main():
    used_passwords = []

    print("Password Strength Analyzer")
    print("-" * 30)

    while True:
        password = input("\nEnter a password (or 'quit' to exit): ")

        if password.lower() == "quit":
            break

        if password in used_passwords:
            print("This password was used before. Choose a different one.")
            continue

        used_passwords.append(password)

        strength, score, feedback = check_strength(password)

        print(f"Strength : {strength} ({score}/6)")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  - {tip}")

        print(f"Suggested password: {suggest_password()}")


main()
