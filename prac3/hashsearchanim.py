import random
import time
import tkinter as tk

# create a list of random integers
arr = [random.randint(0, 50) for i in range(20)]

# create a hash table from the array
hash_table = {}
for i in range(len(arr)):
    if arr[i] in hash_table:
        hash_table[arr[i]].append(i)
    else:
        hash_table[arr[i]] = [i]

# define the hash search function
def hash_search(arr, hash_table, x):
    if x in hash_table:
        return hash_table[x]
    else:
        return None

# create the tkinter window and canvas
root = tk.Tk()
root.state('zoomed')
canvas = tk.Canvas(root, width=1000 , height=500)
canvas.pack()

# create the rectangles to represent the array elements
rectangles = []
for i in range(len(arr)):
    rect = canvas.create_rectangle(70 + i*40, 230, 110 + i*40, 270, fill='blue')
    value = canvas.create_text(90 + i*40, 250, text=str(arr[i]), fill='white')
    rectangles.append((rect, value))

# create the search button and input field
search_button = tk.Button(root, text='Search')
search_button.pack(side='left')
search_input = tk.Entry(root)
search_input.pack(side='left')

# create the reset button
reset_button = tk.Button(root, text='Reset')
reset_button.pack(side='left')

# define the reset function
def reset_animation():
    for i in range(len(arr)):
        canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.itemconfig(rectangles[i][1], fill='white')
    canvas.update()

# bind the reset button to the reset_animation function
reset_button.config(command=reset_animation)

# define the search animation function
def search_animation():
    x = int(search_input.get())
    positions = hash_search(arr, hash_table, x)
    if positions:
        for i in range(len(arr)):
            if i in positions:
                canvas.itemconfig(rectangles[i][0], fill='green')
                canvas.itemconfig(rectangles[i][1], fill='white')
            else:
                canvas.itemconfig(rectangles[i][0], fill='blue')
                canvas.itemconfig(rectangles[i][1], fill='white')
    else:
        tk.messagebox.showinfo('Result', f'{x} not found')
    canvas.update()

# bind the search button to the search_animation function
search_button.config(command=search_animation)

# start the tkinter main loop
root.mainloop()
