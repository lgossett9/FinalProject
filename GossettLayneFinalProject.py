import shutil
import tkinter as tk
from PIL import Image, ImageTk

def open_sandwich_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Sandwich Menu")

    # Add sandwich images and labels
    sandwich_image = Image.open("sandwich.jpg")
    sandwich_photo = ImageTk.PhotoImage(sandwich_image)
    sandwich_label = tk.Label(menu_window, image=sandwich_photo, text="Classic Sandwich")
    sandwich_label.pack(pady=20)

    # Add buttons for selecting sandwiches
    def select_sandwich():
        selected_sandwich = "Classic Sandwich"
        open_order_summary(selected_sandwich)
    sandwich_button = tk.Button(menu_window, text="Select", command=select_sandwich)
    sandwich_button.pack(pady=10)

def open_order_summary(selected_sandwich):
    summary_window = tk.Toplevel(root)
    summary_window.title("Order Summary")

    # Display the selected sandwich and order details
    order_label = tk.Label(summary_window, text=f"You ordered: {selected_sandwich}")
    order_label.pack(pady=20)

    # Add buttons for order submission and navigation
    def submit_order():
        # Implement order submission logic
        pass
    submit_button = tk.Button(summary_window, text="Submit Order", command=submit_order)
    submit_button.pack(pady=10)

    def go_back_to_menu():
        summary_window.destroy()
        open_sandwich_menu()
    back_button = tk.Button(summary_window, text="Back to Menu", command=go_back_to_menu)
    back_button.pack(pady=10)

def select_sandwich():
    if selected_sandwich is None:
        # Display an error message or prompt the user to select a sandwich
        return
    open_order_summary(selected_sandwich)

# Create the main window
root = tk.Tk()
root.title("Sandwich Ordering App")

# Add a logo or title
title_label = tk.Label(root, text="Welcome to Sandwich Ordering App")
title_label.pack(pady=20)

# Create navigation buttons
menu_button = tk.Button(root, text="View Menu", command=open_sandwich_menu)
menu_button.pack(pady=10)

order_button = tk.Button(root, text="View Order", command=open_order_summary)
order_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
shutil.make_archive