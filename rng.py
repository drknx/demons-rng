import random
import tkinter as tk
import math

luck = random.randint(0, 137) # higher the number, lower the luck

best_result = None


# rol
def roll_rng():
    global best_result
    max_value = 10**10
    scaled_random = random.random() ** luck
    result = int(scaled_random * max_value) + 2
    percentage = round(100 * (1 / luck), 2)
    if best_result is None or result > best_result:
        best_result = result
    label_result.config(text=f"You rolled: 1 in a {result:,}\nBest: 1 in a {best_result:,}\n")


# cool graph ez
root = tk.Tk()
root.title("demon's RNG")
root.geometry("1250x800")
root.configure(bg="black")

label_title = tk.Label(root, text="demon's RNG", font=("Montserrat", 42), fg="red", bg="black")
label_title.pack(pady=20)

label_result = tk.Label(root, text="", font=("Montserrat", 32), fg="red", bg="black")
label_result.pack(pady=20)

button_roll = tk.Button(root, text="roll", command=roll_rng, font=("Montserrat", 28), bg="red", fg="black")
button_roll.pack(pady=10)

luck_title = tk.Label(root, text=f"natural luck multiplier (lower is worse): {round(100 * (1 / luck), 2)}%", font=("Montserrat", 42), fg="red", bg="black")
luck_title.pack(pady=10)

root.mainloop()
