#!/usr/bin/python3
"""Contains a class 'Node'"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """initializes it parameters.

        Args:
            data: the data
            next_node: reference to the next_node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data in a node."""
        return self.__data

    @data.setter
    def data(self, data):
        """Sets the data in a node.

        Raises:
            TypeError: if data is not an integer

        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Gets the next_node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Gets the next_node in the list.

        Raises:
            TypeError: if next node is not a Node object

        """
        if next_node is not None and type(next_node).__name__ != 'Node':
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize private variable."""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position
        in the list (increasing order) """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            if self.__head.data > new_node.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                walk = self.__head
                while walk.next_node is not None:
                    if walk.next_node.data > new_node.data:
                        break
                    walk = walk.next_node

                new_node.next_node = walk.next_node
                walk.next_node = new_node

    def __str__(self):
        """representation of the string."""
        if self.__head is not None:
            current = self.__head
            if current.next_node is None:
                result = str(current.data)
            else:
                result = str(current.data) + '\n'
            while current.next_node is not None:
                current = current.next_node
                if current.next_node is None:
                    result += str(current.data)
                else:
                    result += str(current.data) + '\n'

            return result
        else:
            return ""
