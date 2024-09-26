import threading
import tkinter as tk
import time
from tkinter import messagebox

flag = False
popup_shown = False


def check_time():
    global flag, popup_shown
    if flag and not popup_shown:
        try:
            hour = int(hour_entry.get())
            minute = int(minute_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer")
            return

        current_hour = time.localtime().tm_hour
        current_minute = time.localtime().tm_min
        if current_hour == hour and current_minute == minute:
            popup_shown = True
            threading.Thread(target=show_popup).start()


def show_popup():
    global  flag
    messagebox.showinfo("提醒", "time's up")
    flag = False

def button_pressed():
    global flag,popup_shown
    popup_shown = False
    flag = True

'''
Update the time in the window. The time should always be there.
'''
def update_time():
    global flag, popup_shown
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    check_time()
    print("flag: " + str(flag) + "; popup_shown: " + str(popup_shown))
    root.after(1000, update_time)

# Initialize the window
root = tk.Tk()

# Create the time label to show the current time
time_label = tk.Label(root, font="Helvetica 40 bold", fg="black", bg="white")
time_label.pack()


# Create entry1 for user to enter the alarm hour
hour_label = tk.Label(root, text="Hour", font="Helvetica 15 bold", fg="black", bg="white")
hour_label.pack(side="left")
hour_entry = tk.Entry(root, font="Helvetica 15")
hour_entry.pack(side="left")

# Create entry2 for user to enter the alarm minute
minute_label = tk.Label(root, text="Minute", font="Helvetica 15 bold", fg="black", bg="white")
minute_label.pack(side="left")
minute_entry = tk.Entry(root, font="Helvetica 15")
minute_entry.pack(side="left")

# Create button
start_button = tk.Button(root, text="开始", command=button_pressed)
start_button.pack(side="left")

update_time()  # Start the time update loop

root.mainloop()