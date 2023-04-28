import random
import tkinter as tk
import sys

# create a list of random integers
#arr = [random.randint(0, 100) for i in range(20)]
arr=eval(sys.argv[1])

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
search_button = tk.Button(root, text='Search',font=(25))
search_button.place(x=500, y=350)
search_input = tk.Entry(root, font=(35))
search_input.place(x=600, y=350)
result=tk.Label(root,)

# create the reset button
reset_button = tk.Button(root, text='Reset', font=(25))
reset_button.place(x=850, y=350)

#quit
def close():
    root.destroy()
    
quit_button=tk.Button(root,text='Quit',command=close,font=(20))
quit_button.place(x=950, y=350)

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
    x = (search_input.get())
    found = False
    pos=[]
    for i in range(len(arr)):
        # if found == True:
        #     pos.append(i) 
        if arr[i] == x:
            found = True
            pos.append(i+1) 
            canvas.itemconfig(rectangles[i][0], fill='green')
            canvas.itemconfig(rectangles[i][1], fill='black')
        else:
            canvas.itemconfig(rectangles[i][0], fill='red')
            canvas.itemconfig(rectangles[i][1], fill='white')
        canvas.update()
        canvas.after(100)
    if not found:
        not_found_label = tk.Label(root, text=f'{x} not found')
        not_found_label.pack()
    else:
        found_label = tk.Label(root, text=f'{x} found at {pos}')
        found_label.pack()        
        

# bind the search button to the search_animation function
search_button.config(command=search_animation)

# start the tkinter main loop
root.mainloop()
