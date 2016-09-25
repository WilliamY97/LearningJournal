def RemoveDups(ll):
    current = ll.next
    seen = set(current.value)
    
    while ll.next != None:
        if ll.next in seen:
            ll.next = ll.next.next
        else:
            seen.add(ll.next)
    
    return ll
