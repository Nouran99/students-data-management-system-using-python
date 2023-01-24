class Student:
    def __init__(self, name, id, group):
        self.next = None
        self.prev = None
        self.name = name
        self.id = id
        self.group = group

    def __repr__(self):
        return f"{self.name} , {self.id} , {self.group}"


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def Append(self, std):
        stud = std
        if self.head is None:
            self.head = self.tail = stud
        else:
            self.tail.next = stud
            stud.prev = self.tail
            self.tail = stud

    def Display(self):
        if self.head is not None:
            new_std = self.head
            while new_std is not None:
                print(new_std)
                new_std = new_std.next
        else:
            print("Dear, List is empty !!")

    def InsertByPos(self, std, pos):
        if pos ==1 :
            self.Append(std)
        else:
            curr= self.head
            i=1
            while curr.next is not None and i< pos -1 :
                curr = curr.next
                i += 1
            if curr.next is not None:
                curr.next.prev = std
                std.next = curr.next
                curr.next = std
                std.prev = curr
            else :
                self.tail.next = std
                std.prev = self.tail
                self.tail = std




    def SearchByName(self, nam):
        name = nam.lower()
        if self.head is not None:
            curr = self.head
            while curr.name.lower() != name and curr.next is not None:
                curr = curr.next
            if curr.next is not None:
                print(curr)
            else :
                print("I can't find any data")

    def DeleteAll(self):
        self.head = self.tail = None

    def DeleteByID(self, d):
        if self.head is not None:
            curr = self.head
            while curr.id != d and curr.next is not None:
                curr = curr.next
            if curr.next is None:
                print("no thing to delete")
            else:
                if curr == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    if curr == self.head :
                        self.head = self.head.next
                        self.head.prev = None
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev =curr.prev


std1 = Student('Ahmed', 1, 'D')
std2 = Student('mona', 2, 'A')
std3 = Student('ali', 3, 'B')
std4 = Student('Mohamed', 4, 'B')
std5 = Student('nour', 5, 'D')
std6 = Student('Rami', 6, 'C')
std7 = Student('hossam', 7, 'A')
std8 = Student('Zyad', 8, 'D')

ll = LinkedList()
ll.Append(std1)
ll.Append(std3)
ll.Append(std5)
ll.Append(std7)
ll.Display()
print ("\n\n")
ll.InsertByPos(std2, 2)
ll.InsertByPos(std4,4)
ll.InsertByPos(std6,6)
ll.InsertByPos(std8,8)
ll.Display()
print ("\n\n")
ll.SearchByName('HOSSAM')
ll.SearchByName('Rania')
print ("\n\n")
ll.DeleteByID(1)
ll.Display()
print ("\n\n")
ll.DeleteByID(3)
ll.Display()
print ("\n\n")

ll.DeleteByID(8)
ll.Display()
print ("\n\n")
ll.DeleteByID(3)
print ("\n\n")
ll.DeleteAll()
ll.Display()
