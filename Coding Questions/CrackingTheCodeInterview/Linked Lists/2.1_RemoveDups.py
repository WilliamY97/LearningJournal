from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll

ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

