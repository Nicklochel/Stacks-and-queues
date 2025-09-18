# node.py
"""
Simple Node class for linked structures.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value!r})"
