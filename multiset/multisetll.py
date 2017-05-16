import copy
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
    inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from node import Node


# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.data == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.data != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        Removes all nodes from the multiset and returns values as a list.
        """
        lst = []
        while self._head != None:
            lst.append(self._head.data)
            self._head = self._head.next
        return lst

    def split_half(self):
        """
        приймає посилання на однозв’язаний список, ділить його на дві частини і повертає
        посилання на ці частинеи. Якщо в структурі тільки один вузол то метод повинен повертати None.
        """
        second_half = Multiset()
        counter = 0
        multiset_copy = copy.deepcopy(self)
        while multiset_copy._head != None:
            multiset_copy._head = multiset_copy._head.next
            counter += 1
        if counter == 1:
            return None
        for i in range(counter//2):
                second_half.add(self._head)
                self._head = self._head.next
        return self, second_half


mynode = Multiset()
mynode.add(3)
mynode.add([3, 4])
mynode.add("T")
mynode.delete("r")
print(mynode.remove_all())
print(mynode._head.data)
print(mynode.__contains__(3))
"""
Доповнити реалізацію Multiset ADT наступними методами:
a. remove_all(head), приймає посилання на однозв’язаний список, по черзі видаляє всі його вершини та
повертає значення.
b. split_half(head), приймає посилання на однозв’язаний список, ділить його на дві частини і повертає
посилання на ці частинеи. Якщо в структурі тільки один вузол то метод повинен повертати None.
"""
