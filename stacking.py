import sys

class stack:
    def __init__(self, stacksize):
        self.mystack = []
        self.stacksize = stacksize

    def isfull(self):
        if len(self.mystack) == self.stacksize:
            return True
        else:
            return False

    def isempty(self):
        if len(self.mystack) == 0:
            return True
        else:
            return False

    def push(self, value):
        if self.isfull():
            print("Stack is full")
        else:
            self.mystack.append(value)
            print("Element pushed:", value)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            value = self.mystack.pop()
            print("Element popped:", value)

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("TOP ELEMENT =", self.mystack[-1])

    def deletstack(self):
        self.mystack = []
        print("Stack is deleted")

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Elements in stack are:", self.mystack)


size = int(input("Enter the size of stack: "))
obj = stack(size)

while True:
    print("\n1. Push operation")
    print("2. Pop operation")
    print("3. Peek operation")
    print("4. Isfull operation")
    print("5. Isempty operation")
    print("6. Delete stack operation")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to push in stack: "))
        obj.push(value)

    elif choice == 2:
        obj.pop()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        print("Stack is full:", obj.isfull())

    elif choice == 5:
        print("Stack is empty:", obj.isempty())

    elif choice == 6:
        obj.deletstack()

    elif choice == 7:
        obj.display()

    elif choice == 8:
        print("Program exited")
        sys.exit()

    else:
        print("Invalid choice")