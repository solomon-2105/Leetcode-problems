class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_at_beginning(self,data):
        new_node=Node(data)
        print(f"element {new_node.data} has been added in the beginning")
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def add_at_position(self,data,pos):
        new_node=Node(data)
        #if list is empty or position is at beginning
        if pos==1 or self.head is None:
            print(f"element {new_node.data} has been added at position {pos}")
            new_node.next=self.head
            if self.head is not None:
                self.head.prev=new_node
            self.head=new_node
            return
        #if list ain't empty bitch
        cnt=1
        current=self.head
        while current is not None and cnt<pos-1: #we stop 1 place before the actual position
            cnt+=1
            current=current.next
        if current is None:
            print("position is beyond range")
            return
        print(f"element {new_node.data} is added at position {pos}")
        new_node.next=current.next 
        new_node.prev=current
        if current.next is not None:
            current.next.prev=new_node
        current.next=new_node

    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            print(f"element {new_node.data} has been added at the end")
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        print(f"element {new_node.data} has been added at the end")
        new_node.prev=current
        current.next=new_node

    def add_before_value(self, k, x):
        new_node = Node(k)

        # Case 1: empty list
        if self.head is None:
            print("empty linked list")
            return

        # Case 2: target is the head
        if self.head.data == x:
            print(f"element {new_node.data} has been added before {x}")
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Case 3: target is somewhere after the head
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                print(f"element {new_node.data} has been added before {x}")
                new_node.next = current.next
                current.next.prev = new_node
                new_node.prev = current
                current.next = new_node
                return
            current = current.next

        # Case 4: target not found
        print(f"value {x} not found in the linked list")


    def add_after_value(self, k, x):
        new_node = Node(k)

        # Case 1: empty list
        if self.head is None:
            print("empty linked list")
            return

        # Case 2: traverse to find node with value x
        current = self.head
        while current is not None:
            if current.data == x:
                print(f"element {new_node.data} has been added after {x}")
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        # Case 3: value not found
        print(f"value {x} not found in the linked list")


    def delete_head(self):
        if self.head is None:
            print("empty linked list")
            return
        current=self.head
        print(f"deleted the head node {current.data}")
        self.head=self.head.next
        if self.head is not None:
            self.head.prev=None

    def delete_tail(self):
        if self.head is None: #for 0 elements
            print("empty linked list")
            return
        if self.head.next is None: #for one element
            print(f"element {self.head.data} is deleted")
            self.head=None
            return
        current=self.head
        while current.next.next is not None: #stop at last "nunchi -_- " second element
            current=current.next 
        print(f"element {current.next.data} has been deleted (tail node)")
        current.next=None 

    def delete_pos(self,pos):
        if self.head is None:
            print("empty linked list")
            return 
        if pos == 1:
            print(f"element {self.head.data} has been deleted")
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            return
        cnt=1
        current=self.head
        while current is not None and cnt<pos-1: #we stop 2 places before the actual position
            cnt+=1
            current=current.next
        if current is None or current.next is None:
            print("position is beyond range")
            return
        print(f"element {current.next.data} has been deleted")
        current.next=current.next.next
        current.next.prev=current if current.next else None
        
    def delete_particular(self,brr):
        if self.head is None:
            print("empty linked list")
            return 
        if self.head.data==brr:
            print(f"element {self.head.data} has been deleted")
            self.head=self.head.next
            self.head.prev=None if self.head else None
            return
        current=self.head
        while current.next is not None:
            if current.next.data==brr:
                print(f"element {current.next.data} has been deleted")
                current.next=current.next.next
                current.next.prev=current if current.next else None
                return
            current=current.next
        print("element is not found in the list")

    def display(self):
        current=self.head
        if current is None:
            print("List is empty")
            return
        while current is not None:
            print(current.data, end=" <-> ")
            current=current.next
        print("None")

    def count_no_of_elements(self):
        current=self.head
        c=0
        if current is None:
            print("List is empty")
            return
        while current is not None:
            c+=1
            current=current.next
        print(f"{c} elements in the list")

    def search_an_element(self,key):
        current=self.head
        if current is None:
            print("List is empty")
            return
        while current is not None:
            if current.data==key:
                print(f"Element {key} found in the list")
                return
            current=current.next
        print(f"Element {key} not found in the list")

ll=LinkedList()
while True:
    print("choose your options: ")
    print("1.add in the beginning\n2.add in the end\n3.add at some position\n4.add k value before x value\n5.add k value after x value\n6.delete head node\n7.delete tail node\n8.delete kth element\n9.delete any particular element\n10.count the number of elements in the linkedlist\n11.display the linkedlist\n12.search an element\n13.terminate the process")
    i=int(input("enter your choice : "))
    if i==1:
        brr=int(input("enter the data : "))
        ll.add_at_beginning(brr)
    elif i==2:
        brr=int(input("enter the data : "))
        ll.add_at_end(brr)
    elif i==3:
        brr=int(input("enter the data : "))
        pos=int(input("enter the position : "))
        ll.add_at_position(brr,pos)
    elif i==4:
        k=int(input("enter k value : "))
        x=int(input("enter x value : "))
        ll.add_before_value(k,x)
    elif i==5:
        k=int(input("enter k value : "))
        x=int(input("enter x value : "))
        ll.add_after_value(k,x)
    elif i==6:
        ll.delete_head()
    elif i==7:
        ll.delete_tail()
    elif i==8:
        pos=int(input("enter the element's position : "))
        ll.delete_pos(pos)
    elif i==9:
        brr=int(input("enter the element to be deleted : "))
        ll.delete_particular(brr)
    elif i==10:
        ll.count_no_of_elements()
    elif i==11:
        ll.display()
    elif i==12:
        brr=int(input("enter the element to be searched : "))
        ll.search_an_element(brr)
    elif i==13:
        break
    else:
        print("give valid inputs in range (1-13) ")
    print()

#output
'''
choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 1
enter the data : 30
element 30 has been added in the beginning

choose your options: 
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 1
enter the data : 20
element 20 has been added in the beginning

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 1
enter the data : 10
element 10 has been added in the beginning

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
10 <-> 20 <-> 30 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 2
enter the data : 40
element 40 has been added at the end

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
10 <-> 20 <-> 30 <-> 40 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 3
enter the data : 25
enter the position : 3
element 25 is added at position 3

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
10 <-> 20 <-> 25 <-> 30 <-> 40 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 4
enter k value : 15
enter x value : 20
element 15 has been added before 20

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
10 <-> 15 <-> 20 <-> 25 <-> 30 <-> 40 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 5
enter k value : 35
enter x value : 30
element 35 has been added after 30

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
10 <-> 15 <-> 20 <-> 25 <-> 30 <-> 35 <-> 40 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 6
deleted the head node 10

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
15 <-> 20 <-> 25 <-> 30 <-> 35 <-> 40 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 7
element 40 has been deleted (tail node)

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
15 <-> 20 <-> 25 <-> 30 <-> 35 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 8
enter the element's position : 3
element 25 has been deleted

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
15 <-> 20 <-> 30 <-> 35 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 9
enter the element to be deleted : 15
element 15 has been deleted

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 11
20 <-> 30 <-> 35 <-> None

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 10
3 elements in the list

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 12
enter the element to be searched : 35
Element 35 found in the list

choose your options:
1.add in the beginning
2.add in the end
3.add at some position
4.add k value before x value
5.add k value after x value
6.delete head node
7.delete tail node
8.delete kth element
9.delete any particular element
10.count the number of elements in the linkedlist
11.display the linkedlist
12.search an element
13.terminate the process
enter your choice : 13
'''