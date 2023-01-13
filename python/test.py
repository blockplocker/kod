import tkinter as tk

root = tk.Tk()
root.title("My Game")
root.geometry("800x500")

counter = 0
counter_var = tk.StringVar()
counter_var.set(counter)

def increase_counter(counter):
    counter = counter + 1
    counter_var.set(counter)

label = tk.Label(root, textvariable=counter_var)
label.pack()

button = tk.Button(root, text="Increase Counter", command=lambda: increase_counter(counter))
button.pack()

root.mainloop()
