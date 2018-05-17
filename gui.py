import tkinter as tk
# For some reason, the above doesn't import messagebox, so have to import separately.
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import tkinter.filedialog as fd

import backup as b
import logsheet as log
#import os

root = tk.Tk()
root.title("File back up utility")

# Make a frame to group back up functions
backup_frame = tk.LabelFrame(master=root, text="Back up")
backup_frame.grid(row=5, column=2) # Sets maximum number of rows and cols
        
# Button to set data directory
def browse_data_dir():
    global data_dir
    data_dir = fd.askdirectory(parent=backup_frame)
    data_dir_display.config(text=data_dir)
    
data_dir_button = tk.Button(backup_frame, text="Select data directory", command=browse_data_dir)
data_dir_button.grid(row=0, column=0)
    
# Display data directory
data_dir_display = tk.Label(backup_frame, text=data_dir)
data_dir_display.grid(row=0, column=1)


# Find missing log sheets
log_sheet_name = "logsheet.txt"

def find_missing_logsheets():
    try:
        ignore_file = ".backupignore"
        logsheetreport = log.findlogsheets(data_dir, log_sheet_name, ignore_file)
        log.writelogsheetreport(data_dir, logsheetreport)
    except AssertionError as fail:
        tkmb.showerror(title="User error", message=fail)

find_button = tk.Button(backup_frame, text="Find missing logsheets", command=find_missing_logsheets)
find_button.grid(row=1, column=0)

# Display GUI
root.mainloop()
