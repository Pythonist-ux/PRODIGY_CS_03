import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_error = not any(
        char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for char in password)

    errors = [length_error, uppercase_error,
              lowercase_error, digit_error, special_error]
    error_count = sum(errors)

    if error_count == 0:
        return "Strong", "green"
    elif error_count == 1:
        return "Moderate", "orange"
    else:
        return "Weak", "red"


def check_password():
    password = password_entry.get()
    strength, color = check_password_strength(password)
    feedback_label.config(text=f"Password Strength: {strength}", fg=color)


root = tk.Tk()
root.title("Password Strength Checker")
root.configure(bg="#000000")

poppins_font = tkfont.Font(family="Poppins", size=12)

label = tk.Label(root, text="Enter your password:",
                 fg="white", bg="#000000", font=poppins_font)
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30, font=poppins_font)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength",
                         command=check_password, bg="#444444", fg="white", font=poppins_font)
check_button.pack(pady=10)

feedback_label = tk.Label(root, text="", bg="#000000", font=poppins_font)
feedback_label.pack()

root.mainloop()
