import random
import tkinter as tk
import sys

# create a list of random integers
#arr = [random.randint(0, 100) for i in range(20)]
arr=eval(sys.argv[1])
#arr=[1,25,6,32,7,8]

root = tk.Tk()
root.state('zoomed')
canvas = tk.Canvas(root, width=1000 , height=500)
canvas.pack()

rectangles = []
for i in range(len(arr)):
    rect = canvas.create_rectangle(70 + i*40, 230, 110 + i*40, 270, fill='blue')
    value = canvas.create_text(90 + i*40, 250, text=str(arr[i]), fill='white')
    rectangles.append((rect, value))
    
hashed_dict = {}
for value in arr:
    key = value % 10  # use modulo 10 as the hash function
    if key in hashed_dict:
        hashed_dict[key].append(value)
    else:
        hashed_dict[key] = [value]
print(hashed_dict)

# create the search button and input field
search_button = tk.Button(root, text='Search')
search_button.pack(side='left')
search_input = tk.Entry(root)
search_input.pack(side='left')

#quit
def close():
    root.destroy()
    
quit_button=tk.Button(root,text='Quit',command=close,font=('Arial',20),padx=10,pady=10)
quit_button.pack()

def reset_animation():
    for i in range(len(arr)):
        canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.itemconfig(rectangles[i][1], fill='white')
    canvas.update()

# create the reset button
reset_button = tk.Button(root, text='Reset')
reset_button.pack(side='left')
# bind the reset button to the reset_animation function
reset_button.config(command=reset_animation)

def search_animation():
    reset_animation()
    search_value = int(search_input.get())
    for key, values in hashed_dict.items():
        for i in range(len(values)):
            if values[i] == search_value:
                print(f"The relative key for value {search_value} is '{key}'.")
                rect_idx = arr.index(search_value)
                canvas.itemconfig(rectangles[rect_idx][0], fill='green')
                canvas.itemconfig(rectangles[rect_idx][1], fill='black')
                found_label = tk.Label(root, text=f'{search_value} found at {arr.index(search_value)+1} with key {key}')
                found_label.pack()        
                return
    not_found_label = tk.Label(root, text=f"No key was found for value {search_value}.")
    not_found_label.pack()


# bind the search button to the search_animation function
search_button.config(command=search_animation)

root.mainloop()