import threading
import time
import tkinter as tk
from tkinter import messagebox

'''
always show the time
'''
def update_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=current_time)
        time.sleep(1)

'''
open a new window for alarm setting
'''
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry('300x300')
    new_window.title('New Window')

    # 使用grid布局，将标签和输入框放置在网格中
    hour_label = tk.Label(new_window, text='Hour', font=('Arial', 12))
    hour_label.grid(row=0, column=0, padx=10, pady=10)
    hour_entry = tk.Entry(new_window, font=('Arial', 12))
    hour_entry.grid(row=0, column=1, padx=10, pady=10)

    minute_label = tk.Label(new_window, text='Minute', font=('Arial', 12))
    minute_label.grid(row=1, column=0, padx=10, pady=10)
    minute_entry = tk.Entry(new_window, font=('Arial', 12))
    minute_entry.grid(row=1, column=1, padx=10, pady=10)

    status_label = tk.Label(new_window, text='闹钟未设定', font=('Arial', 12), fg='blue')
    status_label.grid(row=3, columnspan=2, padx=10, pady=10)

    # 创建按钮
    button_start = tk.Button(new_window, text='Start', font=('Arial', 12),
                             command=lambda: start_alarm_thread(hour_entry, minute_entry, status_label))
    button_start.grid(row=2, columnspan=2, pady=20)


'''
open a new window for focus
'''
def open_new_window2():
    new_window2 = tk.Toplevel(root)
    new_window2.geometry('400x500')
    new_window2.title('New Window2')

    # 使用grid布局，将标签和输入框放置在网格中
    hour_label_start = tk.Label(new_window2, text='Hour start', font=('Arial', 12))
    hour_label_start.grid(row=0, column=0, padx=10, pady=10)
    hour_entry_start = tk.Entry(new_window2, font=('Arial', 12))
    hour_entry_start.grid(row=0, column=1, padx=10, pady=10)

    minute_label_start = tk.Label(new_window2, text='Minute start', font=('Arial', 12))
    minute_label_start.grid(row=1, column=0, padx=10, pady=10)
    minute_entry_start = tk.Entry(new_window2, font=('Arial', 12))
    minute_entry_start.grid(row=1, column=1, padx=10, pady=10)

    divide_line_label1 = tk.Label(new_window2, text='=======================', font=12)
    divide_line_label1.grid(row=2, columnspan=2, padx=10, pady=10)

    hour_label_end = tk.Label(new_window2, text='Hour end', font=('Arial', 12))
    hour_label_end.grid(row=3, column=0, padx=10, pady=10)
    hour_entry_end = tk.Entry(new_window2, font=('Arial', 12))
    hour_entry_end.grid(row=3, column=1, padx=10, pady=10)

    minute_label_end = tk.Label(new_window2, text='Minute end', font=('Arial', 12))
    minute_label_end.grid(row=4, column=0, padx=10, pady=10)
    minute_entry_end = tk.Entry(new_window2, font=('Arial', 12))
    minute_entry_end.grid(row=4, column=1, padx=10, pady=10)

    divide_line_label2 = tk.Label(new_window2, text='=======================', font=12)
    divide_line_label2.grid(row=5, columnspan=2, padx=10, pady=10)

    study_time_label = tk.Label(new_window2, text='Study time', font=('Arial', 12))
    study_time_label.grid(row=6, column=0, padx=10, pady=10)
    study_time_entry = tk.Entry(new_window2, font=('Arial', 12))
    study_time_entry.grid(row=6, column=1, padx=10, pady=10)

    rest_time_label = tk.Label(new_window2, text='Break time', font=('Arial', 12))
    rest_time_label.grid(row=7, column=0, padx=10, pady=10)
    rest_time_entry = tk.Entry(new_window2, font=('Arial', 12))
    rest_time_entry.grid(row=7, column=1, padx=10, pady=10)

    divide_line_label3 = tk.Label(new_window2, text='=======================', font=12)
    divide_line_label3.grid(row=8, columnspan=2, padx=10, pady=10)
    # 创建按钮
    button_study_start = tk.Button(new_window2, text='Start', font=('Arial', 12)
                                   , command=lambda : calculate())
    button_study_start.grid(row=9, columnspan=2, padx=10, pady=10)


'''
start the alarm checking in a separate thread
'''
def start_alarm_thread(hour_entry, minute_entry, status_label):
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values for hour and minute")
        return

    # Start a new thread to check the time without blocking the main GUI
    alarm_thread = threading.Thread(target=check_time_until_alarm, args=(hour, minute, status_label))
    alarm_thread.daemon = True
    alarm_thread.start()

'''
check if the current time matches the user-set alarm time
'''
def check_time_until_alarm(hour, minute, status_label):
    status_label.config(text="闹钟已启动，还没到时间")
    while True:
        current_hour = time.localtime().tm_hour
        current_minute = time.localtime().tm_min

        if current_hour == hour and current_minute == minute:
            status_label.config(text="闹钟响了")
            pop_window(status_label)
            break
        time.sleep(2)  # 检查间隔为10秒，避免频繁检查消耗过多资源

'''
pop a window when the alarm goes off
'''
def pop_window(status_label):
    messagebox.showinfo("提醒", "time's up")
    status_label.config(text="闹钟未设定")

'''
calculate the alarm time
'''
def calculate():
    pass

'''
create the UI
'''
# create window root
root = tk.Tk()
root.title("LUUUUKER'S CLOCK")

# set the scale of the root window
# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口应放置的 x 和 y 坐标，以使窗口位于屏幕中心
x = (screen_width - 600) // 2
y = (screen_height - 400) // 2

root.geometry(f"600x500+{x}+{y}")

'''
create frame1 which contains the clock
'''
frame1 = tk.Frame(root, width=580, height=100, bd=5 , relief=tk.GROOVE, padx=5, pady=5)

# set the time_label
time_label = tk.Label(frame1, font=("Helvetica", 30), height=50, width=400, justify=tk.LEFT, background="blue", fg="white")
time_label.pack()

# pack the frame1
frame1.pack_propagate(False)
frame1.pack(padx=10, pady=10, fill='both', expand=False)


'''
create the frame2 which contains several buttons
'''
frame2 = tk.Frame(root, height=300, width=580, bd=5 , relief=tk.GROOVE, padx=5, pady=5)

# set the buttons
button_alarm = tk.Button(frame2, text="闹钟", font=("Helvetica", 30), command=open_new_window)
button_study = tk.Button(frame2, text="专注", font=("Helvetica", 30), command=open_new_window2)

# Update packing to ensure both buttons display properly
button_alarm.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button_study.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# pack the frame2
frame2.pack_propagate(False)
frame2.pack(padx=10, pady=10, fill='both', expand=False)


'''
put time updating function in a separate thread so that it runs independently
'''
time_thread = threading.Thread(target=update_time)
time_thread.daemon = True
time_thread.start()

# Enter the mainloop
root.mainloop()
