from typing import Any, Union

class ListNode:
    
    __slots__ = "prev", "element", "next"
    
    def __init__(self, element : Any, next = None, prev = None) -> None:
        self.element = element
        self.next : Union[ListNode, None] = next
        self.prev : Union[ListNode, None] = prev