from tkinter import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self,data):
        newNode=Node(data)
        if(self.head==None):
            self.head=self.tail=newNode
            self.head.prev=None 
            self.tail.next=None
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
            self.tail.next=None
    
    def __str__(self):
        current_node = self.head
        linked_list_string = ""
        while current_node is not None:
            linked_list_string += str(current_node.data) + "<-->"
            current_node = current_node.next
        linked_list_string+="None"
        return linked_list_string

class LinkedListGUI:
    def __init__(self):
        self.head=None
        self.tail=None
        self.linked_list = DoublyLinkedList()
        
        self.root = Tk()
        self.root.title("Linked List GUI")
        self.root.state("zoomed")
        
        self.input_label = Label(self.root, text="Enter data:")
        self.input_label.pack()
        
        self.input_box = Entry(self.root)
        self.input_box.pack()
        
        self.add_button = Button(self.root, text="Add", command=self.add_data)
        self.add_button.pack()
        
        self.output_label = Label(self.root, text="Linked List:")
        self.output_label.pack()
        
        self.output_text = Text(self.root,height=10,width=100)
        self.output_text.pack()  
        
        self.b_linsearch=Button(self.root,text="Linear Search",command=self.enter_search_value)
        self.b_linsearch.pack()     
        
        self.root.mainloop()
        
    def add_data(self):
        data = self.input_box.get()
        self.linked_list.append(data)
        self.output_text.delete(1.0, END)
        self.output_text.insert(END, str(self.linked_list))
        if self.head is None:  # update the head and tail attributes
            self.head = self.linked_list.head
            self.tail = self.linked_list.tail
        
    def enter_search_value(self):
        self.input_box_search = Entry(self.root)
        self.input_box_search.pack()
        self.search_button = Button(self.root,text="Search",command=lambda:self.linearsearch(self.input_box_search.get()))
        self.search_button.pack()
        
    def linearsearch(self,search):
        pos=1
        flag=0
        current=self.head
        if(self.head==None):
            print("List is empty")
            return
        while(current!=None):
            if(current.data==search):
                flag=1
                break
            current=current.next
            pos+=1
        if(flag==1):
            label_text = "value found at " + str(pos)
            self.found_label = Label(self.root, text=label_text)
            self.found_label.pack()
            print("Value found at node ",pos)
        else:
            self.notfound_label = Label(self.root, text="Value not found")
            self.notfound_label.pack()
            print("Value not found") 
    

if __name__ == '__main__':
    LinkedListGUI()
