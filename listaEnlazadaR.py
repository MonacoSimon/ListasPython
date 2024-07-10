class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, e):
    if head is None:
        return Node(e)
    else:
        head.next = insert(head.next, e)
    return head
def display(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
def delete(head, e):
    if head is None:
        return None

    if head.data == e:
        return head.next
    current = head
    while current.next is not None:
        if current.next.data == e:
            current.next = current.next.next
            return head
        current = current.next
    return head

head = None
head = insert(head, 10)
head = insert(head, 20)
head = insert(head, 30)
head = insert(head, 40)
display(head)
head = delete(head, 40)
print("Después de eliminar 40:")
display(head) 

