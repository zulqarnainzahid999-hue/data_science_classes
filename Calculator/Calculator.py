import tkinter as tk
import math

# ==== FUNCTIONS ====
def click(btn):
    current = display.get()
    if btn == "C":
        display.delete(0, tk.END)
    elif btn == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif btn == "√":
        try:
            result = str(math.sqrt(float(current)))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif btn == "sin":
        result = str(math.sin(math.radians(float(current))))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    elif btn == "cos":
        result = str(math.cos(math.radians(float(current))))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    elif btn == "tan":
        result = str(math.tan(math.radians(float(current))))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    elif btn == "log":
        result = str(math.log10(float(current)))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    else:
        display.insert(tk.END, btn)

# ==== GUI WINDOW ====
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x520")
root.resizable(False, False)

# ==== DISPLAY ====
display = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
display.pack(fill="both")

# ==== BUTTONS FRAME ====
btns_frame = tk.Frame(root)
btns_frame.pack(expand=True, fill="both")

buttons = [
    ["C", "√", "log", "/"],
    ["sin", "cos", "tan", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"]
]

# ==== ADD BUTTONS TO WINDOW ====
for row in buttons:
    frame = tk.Frame(btns_frame)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(
            frame, text=btn, font=("Arial", 18),
            command=lambda x=btn: click(x)
        )
        button.pack(side="left", expand=True, fill="both")

root.mainloop()