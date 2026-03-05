#BMI_CALCULATOR

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get user input
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        # Validate input
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive values")
            return

        # Convert height from cm to meters
        height_m = height_cm / 100

        # Calculate BMI
        bmi = weight / (height_m ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")
#window.resizable(False, False)

# Heading
tk.Label(window, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Weight input
tk.Label(window, text="Weight (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

# Height input
tk.Label(window, text="Height (cm):").pack()
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Calculate button
tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#4CAF50",
    fg="white",
    width=15
).pack(pady=15)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Run the application
window.mainloop()
