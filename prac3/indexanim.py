import random
import tkinter as tk
import tkinter.messagebox as messagebox
import sys

# create a list of random integers and sort it
#arr=eval(sys.argv[1])
arr=[1,6,9,12,15,17,45,67,78,98]

n = len(arr)
index = 0
jump = int(n ** 0.5)
idx = [i for i in range(0, n, jump)]

# create the tkinter window and canvas
root = tk.Tk()
root.state('zoomed')
canvas = tk.Canvas(root, width=1000 , height=500)
canvas.pack()

# create the rectangles to represent the array elements
rectangles = []
for i in range(len(arr)):
    if i%jump==0:
        rect = canvas.create_rectangle(70 + i*40, 230, 110 + i*40, 270, fill='purple')
    else:
        rect = canvas.create_rectangle(70 + i*40, 230, 110 + i*40, 270, fill='blue')
    value = canvas.create_text(90 + i*40, 250, text=str(arr[i]), fill='white')
    rectangles.append((rect, value))

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

# create the reset button
reset_button = tk.Button(root, text='Reset')
reset_button.pack(side='left')

# define the reset function
def reset_animation():
    for i in range(len(arr)):
        if i%jump==0:
            canvas.itemconfig(rectangles[i][0], fill='purple')
        else:
            canvas.itemconfig(rectangles[i][0], fill='blue')
        canvas.itemconfig(rectangles[i][1], fill='white')
    canvas.update()

# bind the reset button to the reset_animation function
reset_button.config(command=reset_animation)

def find_start(x):
    for val in idx:
        if val>=x:
            return idx.index(val) - 2
        
def find_end(x):
    for val in idx:
        if val>=x:
            return idx.index(val) -1




def search_animation():
    reset_animation() # reset the colors of the rectangles
    x = int(search_input.get())
    found = False
    start = find_start(x)
    end = find_end(x)
    print(start,end)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            found = True
            canvas.itemconfig(rectangles[mid][0], fill='green')
            canvas.itemconfig(rectangles[mid][1], fill='black')
            break
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
        for i in range(start, end+1):
            canvas.itemconfig(rectangles[i][0], fill='red')
            canvas.itemconfig(rectangles[i][1], fill='white')
        canvas.update()
        canvas.after(500)
        for i in range(start, end+1):
            if arr[i] == x:
                found = True
                canvas.itemconfig(rectangles[i][0], fill='green')
                canvas.itemconfig(rectangles[i][1], fill='black')
            else:
                canvas.itemconfig(rectangles[i][0], fill='blue')
                canvas.itemconfig(rectangles[i][1], fill='white')
        canvas.update()
        canvas.after

# bind the search button to the search_animation function
search_button.config(command=search_animation)

# start the tkinter main loop
root.mainloop()
