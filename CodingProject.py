import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Layne's Sandwich Shop App")

# Add a logo or title
title_label = tk.Label(root, text="Welcome to Layne's Sandwich Shop")
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