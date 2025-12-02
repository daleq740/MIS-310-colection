import tkinter as tk
from tkinter import messagebox


def calculate_points():
    """
    Calculates and displays the points awarded based on the number
    of books purchased.
    """
    try:
        #gets the number of books
        num_books = int(books_entry.get())

        points = 0
        # sets points
        if num_books < 0:
            # error code
            messagebox.showerror("Error", "Please enter a positive number.")
            result_label.config(text="")
            return
        elif num_books >= 8:
            points = 60
        elif num_books >= 6:  # Covers 6 and 7
            points = 30
        elif num_books >= 4:  # Covers 4 and 5
            points = 15
        elif num_books >= 2:  # Covers 2 and 3
            points = 5
        else:  # Covers 0 and 1
            points = 0

        # shows results
        result_label.config(text=f"You have earned: {points} points")

    except ValueError:
        # Handle non-integer input
        messagebox.showerror("Error", "Invalid input. Please enter a whole number.")
        result_label.config(text="")


root = tk.Tk()
root.title("Serendipity Booksellers Points")
root.geometry("400x200")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(expand=True, fill=tk.BOTH)

# --- Widgets ---


instruction_label = tk.Label(
    main_frame,
    text="Enter the number of books purchased this month:",
    font=("Arial", 12)
)
instruction_label.pack(pady=5)


books_entry = tk.Entry(main_frame, font=("Arial", 12), width=20)
books_entry.pack(pady=5)


calculate_button = tk.Button(
    main_frame,
    text="Calculate Points",
    font=("Arial", 12, "bold"),
    command=calculate_points
)
calculate_button.pack(pady=10)

#displays result
result_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 12, "bold"),
    fg="blue"
)
result_label.pack(pady=5)

root.mainloop()
