import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Calendar Date Picker")
root.geometry("300x300")

def get_date():
    selected_date = cal.get_date()
    selected_date_label.config( text="Selected Date: " +selected_date)

cal = Calendar(root, selectmode="day", date_pattern="dd-mm-yyyy")
cal.pack(pady=10)

select_button = ttk.Button(root, text="Select Date", command=get_date)
select_button.pack(pady=10)
selected_date_label = ttk.Label(root)
selected_date_label.pack(pady=10)




root.mainloop()