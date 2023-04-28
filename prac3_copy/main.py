from tkinter import *
import subprocess


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
  
  
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def print_linked_list(self):
    # Get the linked list input from the Entry widget
        linked_list_input = linked_list_entry.get()

    # Split the input into individual elements using the separator
        separator = ','
        elements = linked_list_input.split(separator)

    # Print all the elements at once
        for data in elements:
            node = Node(data)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                
        linked_list_str=""
        current = self.head
        while current is not None:
            print(current.data)
            linked_list_str+=str(current.data)+"<-->"
            current = current.next
        linked_list_str+="None"
            
        linked_list_label=Label(root,text=linked_list_str,font=('Arial',42))
        linked_list_label.place(x=500, y=190)
        
root=Tk()
root.state("zoomed")

gui=LinkedList()

linked_list_label = Label(root, text="Enter the linked list:",font=('Arial',42),anchor=CENTER,bg='cyan',fg='red')
linked_list_label.place(x=550, y=10)

linked_list_entry = Entry(root,font=('Arial',42))
linked_list_entry.place(x=470, y=100)

#linked_list label
# linked_list_label=Label(root,font=('Arial',42))
# linked_list_label.pack()

print_button = Button(root, text="Print linked list", command=lambda:gui.print_linked_list(),font=('Arial',20),padx=10,pady=10)
print_button.place(x= 550, y=270)

#linear search
linear_path='C:\\Users\\harsh\\Desktop\\MPRPython\\prac3_copy\\linearanim.py'

def open_linear_search_animation():
    elements = linked_list_entry.get().split(',')
    subprocess.Popen(['python', linear_path,str(elements)])
    
linear_button=Button(root,text='Linear Search',command=open_linear_search_animation,font=('Arial',20),padx=10,pady=10)
linear_button.place(x=850, y=270)

#binary search
binary_path='C:\\Users\\harsh\\Desktop\\MPRPython\\prac3_copy\\binaryanim.py'

def open_binary_search_animation():
    elements = [int(e) for e in linked_list_entry.get().split(',')]
    subprocess.Popen(['python', binary_path, str(sorted(elements))])

binary_button=Button(root,text='Binary Search',command=open_binary_search_animation,font=('Arial',20),padx=10,pady=10)
binary_button.place(x=550, y=400)

#hash search
hash_path='C:\\Users\\harsh\\Desktop\\MPRPython\\prac3_copy\\hashanim.py'

def open_hash_search_animation():
    elements = [int(e) for e in linked_list_entry.get().split(',')]
    subprocess.Popen(['python', hash_path, str((elements))])

hash_button=Button(root,text='Hash Search',command=open_hash_search_animation,font=('Arial',20),padx=10,pady=10)
hash_button.place(x=850, y=400)

#index search
index_path='C:\\Users\\harsh\\Desktop\\MPRPython\\prac3_copy\\indexanim.py'

def open_index_search_animation():
    elements = [int(e) for e in linked_list_entry.get().split(',')]
    subprocess.Popen(['python', index_path, str(sorted(elements))])

index_button=Button(root,text='Index Search',command=open_index_search_animation,font=('Arial',20),padx=10,pady=10)
index_button.place(x=550, y=520)

#quit
def close():
    root.destroy()
    
quit_button=Button(root,text='Quit',command=close,font=('Arial',20),padx=10,pady=10)
quit_button.place(x=900,y=520)



root.mainloop()