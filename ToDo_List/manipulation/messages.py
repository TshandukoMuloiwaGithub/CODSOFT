import tkinter as tk
# from tkinter import messagebox

def custom_message_box(title, message, bg_color):
    root = tk.Tk()

    root.withdraw()  # Hide the root window

    custom_box = tk.Toplevel(root)
    custom_box.title(title)
    custom_box.configure(bg=bg_color)

    # Create message label
    message_label = tk.Label(custom_box, text=message, bg=bg_color)
    message_label.pack(padx=10, pady=10)

    # Create an OK button
    ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy)
    ok_button.pack(pady=5)

    # Center the messagebox on the screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() - custom_box.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - custom_box.winfo_reqheight()) / 2
    custom_box.geometry("+%d+%d" % (x, y))

    custom_box.focus_force()
    custom_box.grab_set()
    custom_box.wait_window()

