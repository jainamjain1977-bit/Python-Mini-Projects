import tkinter as tk
from datetime import datetime
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x220")
root.configure(bg="#000")
label = tk.Label(root,font=("comsolas",50,"bold"),bg="#000",fg="#0ff")
label.pack(expand=True)
def tick():
    label.config(text=datetime.now().strftime("%H:%M:%S:%p"))
    root.after(1000,tick)
tick()
root.mainloop()
