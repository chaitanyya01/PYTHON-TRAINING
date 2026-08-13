import sys

class queue:
    def __init__(self, queuesize):
        self.myqueue = []
        self.queuesize = queuesize

    def isfull(self):
        if len(self.myqueue) == self.queuesize:
            return True
        else:
            return False

    def isempty(self):
        if len(self.myqueue) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isfull():
            print("Queue is full")
        else:
            self.myqueue.append(value)
            print("Element inserted:", value)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            value = self.myqueue.pop(0)
            print("Element deleted:", value)

    def peek(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("FRONT ELEMENT =", self.myqueue[0])

    def deletequeue(self):
        self.myqueue = []
        print("Queue is deleted")

    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Elements in queue are:", self.myqueue)


size = int(input("Enter the size of queue: "))
obj = queue(size)

while True:
    print("\n1. Enqueue operation")
    print("2. Dequeue operation")
    print("3. Peek operation")
    print("4. Isfull operation")
    print("5. Isempty operation")
    print("6. Delete queue operation")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to insert in queue: "))
        obj.enqueue(value)

    elif choice == 2:
        obj.dequeue()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        print("Queue is full:", obj.isfull())

    elif choice == 5:
        print("Queue is empty:", obj.isempty())

    elif choice == 6:
        obj.deletequeue()

    elif choice == 7:
        obj.display()

    elif choice == 8:
        print("Program exited")
        sys.exit()

    else:
        print("Invalid choice")