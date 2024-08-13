import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Password Length
        self.length_label = tk.Label(self.root, text="Password Length:", font=('Helvetica', 12))
        self.length_label.pack(pady=10)

        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(self.root, textvariable=self.length_var, font=('Helvetica', 12))
        self.length_entry.pack(pady=10)

        # Checkbuttons for character inclusion
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.upper_check = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_upper)
        self.upper_check.pack(anchor="w", padx=20)

        self.lower_check = tk.Checkbutton(self.root, text="Include Lowercase", variable=self.include_lower)
        self.lower_check.pack(anchor="w", padx=20)

        self.number_check = tk.Checkbutton(self.root, text="Include Numbers", variable=self.include_numbers)
        self.number_check.pack(anchor="w", padx=20)

        self.special_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.include_special)
        self.special_check.pack(anchor="w", padx=20)

        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Display Generated Password
        self.password_entry = tk.Entry(self.root, font=('Helvetica', 14), justify="center")
        self.password_entry.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4 characters.")
            return

        characters = ""
        if self.include_upper.get():
            characters += string.ascii_uppercase
        if self.include_lower.get():
            characters += string.ascii_lowercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
