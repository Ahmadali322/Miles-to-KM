import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('Miles to KM')
window.geometry('500x300')

# Converting Miles to KM
def convert():
    miles = input_int.get()
    km = miles * 1.61
    output.set(f'{miles} Miles is {km} Kilometers')

# Display fromtend
intro_label = ttk.Label(window, text = 'Miles to KM converter', font = 'Calibri 20 bold')
intro_label.pack()

# Displaying Input Field
input_frame = ttk.Frame(window)
input_int = tk.IntVar()
input = ttk.Entry(input_frame, textvariable = input_int)
submit_button = ttk.Button(input_frame, text = 'Convert', command = convert)
input.pack(side = 'left', padx = 5)
submit_button.pack(side = 'left')
input_frame.pack(pady = 17)

# Displaying Output
output = tk.IntVar()
output_label = ttk.Label(window, textvariable = output, font = 'Calibri 15')
output_label.pack()

# Start the window
window.mainloop()
