import random
import tkinter as tk
import sys


# Create a sorted list of random integers
#arr = sorted([random.randint(0, 100) for i in range(20)])
arr=eval(sys.argv[1])
#arr=arr.sort()

# Create the tkinter window and canvas
root = tk.Tk()
root.title('Binary Search Animation')
root.state('zoomed')
canvas = tk.Canvas(root, width=1000 , height=500)
canvas.pack()

# Create the rectangles to represent the array elements
rectangles = []
for i in range(len(arr)):
    rect = canvas.create_rectangle(70 + i*40, 230, 110 + i*40, 270, fill='blue')
    value = canvas.create_text(90 + i*40, 250, text=str(arr[i]), fill='white')
    rectangles.append((rect, value))

# Create the search button and input field
search_button = tk.Button(root, text='Search')
search_button.pack(side='left')
search_input = tk.Entry(root)
search_input.pack(side='left')

# Create the reset button
reset_button = tk.Button(root, text='Reset')
reset_button.pack(side='left')

#quit
def close():
    root.destroy()
    
quit_button=tk.Button(root,text='Quit',command=close,font=('Arial',20),padx=10,pady=10)
quit_button.pack()

# Define the reset function
def reset_animation():
    for i in range(len(arr)):
        canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.itemconfig(rectangles[i][1], fill='white')
    canvas.update()

# Bind the reset button to the reset_animation function
reset_button.config(command=reset_animation)

# Define the binary search animation function
def binary_search_animation(start, end, x):
    
    mid = (start + end) // 2
    if start > end:
        return [False,mid]
    if arr[mid] == x:
        canvas.itemconfig(rectangles[mid][0], fill='green')
        canvas.itemconfig(rectangles[mid][1], fill='black')          
        return [True,mid]
    elif arr[mid] > x:
        for i in range(mid+1, end+1):
            canvas.itemconfig(rectangles[i][0], fill='red')
        for i in range(start, mid+1):
            canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.update()
        canvas.after(1000)
        return binary_search_animation(start, mid-1, x)
    else:
        for i in range(start, mid):
            canvas.itemconfig(rectangles[i][0], fill='red')
        for i in range(mid, end+1):
            canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.update()
        canvas.after(1000)
        return binary_search_animation(mid+1, end, x)

# Define the search animation function
def search_animation():
    x = int(search_input.get())
    found = binary_search_animation(0, len(arr)-1, x)
    if  found[0]==False:
        not_found_label = tk.Label(root, text=f'{x} not found')
        not_found_label.pack()
    else:
        found_label = tk.Label(root, text=f'{x} found at {found[1]+1}')
        found_label.pack() 

# Bind the search button to the search_animation function
search_button.config(command=search_animation)

# Start the tkinter main loop
root.mainloop()
