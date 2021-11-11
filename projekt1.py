from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        cur = self.head
        total = 0
        while cur != None:
            total += 1
            cur = cur.next
        return total

    def __str__(self):
        current = self.head
        list1 = []
        if self.head is None:
            print("Lista jest pusta")
            return
        while current.next != None:
            list1.append(str(current.value))
            current = current.next
        list1.append(str(current.value))
        list2 = ' -> '.join(list1)
        return list2

    def push(self, value: Any) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append(self, value: Any) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def node(self, at: int) -> Node:
        current = self.head
        for i in range(at):
            current = current.next
        return current.value

    def insert(self, value: Any, after: Node) -> None:
        current = self.head
        while current.next != None:
            if after == current.value:
                newNode = Node(value)
                temp = current.next
                current.next = newNode
                newNode.next = temp
            current = current.next

    def pop(self) -> Any:
        first = self.head
        self.head = self.head.next
        return first.value

    def remove_last(self) -> Any:
        current = self.head
        last = self.tail
        while current.next.next != None:
            current = current.next
        current.next = None
        self.tail = current
        return last.value

    def remove(self, after: Node):
        if self.head is None:
            print("Pusta lista")
            return
        current = self.head
        while current.value != after:
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next


list_ = LinkedList()

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

# wstawi nowy węzeł tuż za węzłem wskazanym w parametrze
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

# usunie pierwszy element z listy i go zwróci
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element == returned_first_element

# usunie ostatni element z listy i go zwróci
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

# usunie z listy następnik węzła przekazanego w parametrze
second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        current = self._storage.head
        list1 = []
        if self._storage.head == None:
            print("Stos jest pusty")
        while current != None:
            list1.append(str(current.value))
            current = current.next
        stos = '\n'.join(list1)
        return stos

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1

assert len(stack) == 2


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        current = self._storage.head
        list1 = []
        if self._storage.head == None:
            print("Kolejka jest pusta")
        while current != None:
            list1.append(str(current.value))
            current = current.next
        kolejka = ', '.join(list1)
        return kolejka

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2