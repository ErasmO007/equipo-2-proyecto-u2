import ds_queue
import ds_stack
import ds_linkedlist

myQueue= ds_queue.Queue()
myStack= ds_stack.Stack()
myLinkedlist= ds_linkedlist.LinkedList()

show_menu = True

def main_menu():
    global show_menu
    print("****Welcome to the main menu****")
    print("Choose the structure to use :")
    print("1. Queue")
    print("2. Stack")
    print("3. Linked List ")
    print("Q to quiet menu")

    option = input("Choose your option: ")

    if option=="1":
       menu_queue()
    elif option == "2":
       menu_stack()
    #Stack
    elif option=="3":
       menu_linkedList()
    #Linked list
    else:
      print("Invalid option, try again")
      main_menu()




def menu_queue():
    global show_menu
    print("What would you like to do? :")
    print("1. Enqueue element")
    print("2. Dequeue element")
    print("3. Peek last element")
    print("R to return to the main menu")
    print("Q to quit Menu")

    queueOption = input("Choose your option: ")

    if queueOption =="1":
      myQueue.enqueue(input("Element to enqueue"))
    elif queueOption=="2":
      myQueue.dequeue()
    elif queueOption=="3":
      print(myQueue.peek())
    elif queueOption.upper() == "R":
       main_menu()
    elif queueOption.upper() == "Q":
       print("Stop running menu     ):")
       show_menu = False
    else:
      print("Invalid option, try again")
      menu_queue()
    menu_queue()




def menu_stack():
    global show_menu
    print("What would you like to do? :")
    print("1. Push element")
    print("2. Pop element")
    print("3. Peek last e")
    print("R to Return to the main menu")
    print("Q to quit Menu")

    stackOption = input("Choose your option: ")

    if stackOption =="1":
      myStack.push(input("Element to push"))
    elif stackOption=="2":
      print(myStack.pop())
    elif stackOption=="3":
       print(myStack.peek())
    elif stackOption.upper() == "R":
       main_menu()
    elif stackOption.upper()== "Q":
       print("Stop running menu     ):")
       show_menu = False
    else:
      print("Invalid option, try again")
      menu_stack()



def menu_linkedList():
    global show_menu
    print("What would you like to do? :")
    print("1. insert at end")
    print("2. insert at beginning")
    print("3. insert after node")
    print("4. delete node")
    print("5. Display elements")
    print("R to Return to the main menu")
    print("Q to quit menu")

    linkedListOption = input("Choose your option: ")

    if linkedListOption == "1":
      myLinkedlist.insert_at_end(input("Element to insert at end: "))
    elif linkedListOption=="2":
      a=input("Element that insert at begin:")
      myLinkedlist.insert_at_beginning(a)
    elif linkedListOption=="3":
      data=input("Element to insert: ")
      target=input("after node: ")
      myLinkedlist.insert_after_node(target, data)
    elif linkedListOption=="4":
      a=input("Insert the node that want delate")
      myLinkedlist.delete_node(a)
    elif linkedListOption=="5":
      myLinkedlist.display()
    elif linkedListOption.upper() == "R":
       main_menu()
    elif linkedListOption.upper() == "Q":
       show_menu = False
    else:
      print("Invalid Option, try again ")
      menu_linkedList()
    menu_linkedList()

while show_menu:
   main_menu()







