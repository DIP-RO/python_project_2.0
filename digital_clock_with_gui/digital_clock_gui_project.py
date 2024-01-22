import tkinter as tk
from time import strftime, localtime

def update_time():
    current_time = strftime('%H:%M:%S %p', localtime())
    current_hour = strftime('%H', localtime())
    current_minute = strftime('%M', localtime())
    current_date = strftime('%Y-%m-%d', localtime())

    label_time.config(text=current_time)
    label_hour.config(text=f'Hour: {current_hour}')
    label_minute.config(text=f'Minute: {current_minute}')
    label_date.config(text=f'Date: {current_date}')

    label_time.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Configure the window size and remove the resizing option
root.geometry('400x200')
root.resizable(False, False)

# Create labels to display the time, hour, minute, and date
label_time = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_time.pack(anchor='center', pady=10)

label_hour = tk.Label(root, font=('calibri', 14), background='black', foreground='white')
label_hour.pack()

label_minute = tk.Label(root, font=('calibri', 14), background='black', foreground='white')
label_minute.pack()

label_date = tk.Label(root, font=('calibri', 14), background='black', foreground='white')
label_date.pack()

# Call the update_time function to update the time and other information
update_time()

# Run the main loop
root.mainloop()
