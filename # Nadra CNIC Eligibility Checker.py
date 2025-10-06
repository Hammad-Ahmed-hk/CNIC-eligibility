# Nadra CNIC Eligibility Checker
import tkinter as tk
from tkinter import messagebox

def check_eligibility(event=None):  # Allow an optional event parameter for binding
    name = entry_name.get()
    try:
        age = int(entry_age.get())
        
        # Store name and age in a file
        with open('Hamizzzzz.pdf', 'a') as file:
            file.write(f"Name: {name}, Age: {age}\n")

        if age >= 18:
            message = f"{name}, you are eligible for CNIC."
            result_label.config(text=message, fg="green")
        else:
            remaining_years = 18 - age
            message = f"{name}, you are not eligible for CNIC. You need {remaining_years} more year(s)."
            result_label.config(text=message, fg="red")

        # Reset fields for the next user after a brief delay
        root.after(3000, reset_fields)  # Wait for 3 seconds before resetting
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid age.")

def reset_fields():
    entry_name.delete(0, tk.END)  # Clear the name entry
    entry_age.delete(0, tk.END)   # Clear the age entry
    result_label.config(text="")   # Clear the result label
    entry_name.focus_set()          # Set focus back to the name entry

def clear_data():
    reset_fields()  # Call reset_fields to clear the user inputs

def move_to_age(event=None):
    entry_age.focus_set()  # Move focus to the age entry field

# Create the main window
root = tk.Tk()
root.title("[Welcome to NADRA Pakistan]")

# Create a frame to contain all widgets with a background color
frame = tk.Frame(root, padx=15, pady=15, bg="#87CEEB")  # Light SKB background
frame.pack(padx=15, pady=15)

# Title label with a custom font and color
title_label = tk.Label(frame, text="WELCOME TO NADRA", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#00008b")  # Dark blue text
title_label.pack(pady=15)

# Create and place labels and entry fields with a background color
label_name = tk.Label(frame, text="Enter your Name:", bg="#f0f8ff", font=("Arial", 14))
label_name.pack(pady=10)

entry_name = tk.Entry(frame, font=("Arial", 14))
entry_name.pack(pady=10)

label_age = tk.Label(frame, text="Enter your Age:", bg="#f0f8ff", font=("Arial", 14))
label_age.pack(pady=10)

entry_age = tk.Entry(frame, font=("Arial", 14))
entry_age.pack(pady=10)

# Create a button to check eligibility with a custom color
check_button = tk.Button(frame, text="Generate Message", command=check_eligibility, 
                         bg="#4caf50", fg="white", font=("Arial", 14, "bold"))  # Green background, white text
check_button.pack(pady=20)
# Create a label for displaying the result
result_label = tk.Label(frame, text="", font=("Arial", 14), bg="#f0f8ff")
result_label.pack(pady=10)

# Bind the Enter key to the functions
entry_name.bind('<Return>', move_to_age)  # Move to age entry on Enter in name entry
entry_age.bind('<Return>', check_eligibility)  # Check eligibility on Enter in age entry

# Start the GUI main loop
root.mainloop()