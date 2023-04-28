import tkinter as tk
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def to_list(self):
        out_list = []
        curr_node = self.head
        while curr_node is not None:
            out_list.append(curr_node.data)
            curr_node = curr_node.next
        return out_list

def merge_linked_lists(llist1, llist2):
    merged_list = LinkedList()
    curr_node1 = llist1.head
    curr_node2 = llist2.head
    while curr_node1 is not None and curr_node2 is not None:
        if curr_node1.data < curr_node2.data:
            merged_list.append(curr_node1.data)
            curr_node1 = curr_node1.next
        else:
            merged_list.append(curr_node2.data)
            curr_node2 = curr_node2.next
    while curr_node1 is not None:
        merged_list.append(curr_node1.data)
        curr_node1 = curr_node1.next
    while curr_node2 is not None:
        merged_list.append(curr_node2.data)
        curr_node2 = curr_node2.next
    return merged_list

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.llist1 = LinkedList()
        self.llist1.append(1)
        self.llist1.append(3)
        self.llist1.append(5)

        self.llist2 = LinkedList()
        self.llist2.append(2)
        self.llist2.append(4)
        self.llist2.append(6)

        self.merged_list = merge_linked_lists(self.llist1, self.llist2)
        self.display_linked_lists()

    def display_linked_lists(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(200, 50, text="Linked List 1:")
        self.display_linked_list(self.llist1, 200, 80)
        self.canvas.create_text(600, 50, text="Linked List 2:")
        self.display_linked_list(self.llist2, 600, 80)
        self.canvas.create_text(400, 300, text="Merged Linked List:")
        self.display_linked_list(self.merged_list, 400, 330)
        self.master.update()
        time.sleep(1)

    def display_linked_list(self, llist, x, y):
        curr_node = llist.head
        while curr_node is not None:
            self.canvas.create_text(x, y, text=curr_node.data, font=("Helvetica", 14))
            if curr_node.next is not None:
                self.canvas.create_line(x + 20, y + 10, x + 80, y + 10, width=2)
            curr_node = curr_node.next
            y += 30

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    root.mainloop()
   
