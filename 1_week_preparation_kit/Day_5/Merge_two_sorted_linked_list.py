"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    # Write your code here

    dummy = SinglyLinkedListNode(0)
    current = dummy

    # While neither is None
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1= head1.next

        else:
            current.next = head2
            head2= head2.next

        current = current.next
        
    # when head2 is None
    while head1:
        current.next = head1
        head1 = head1.next
        current = current.next
        
    # when head1 is None
    while head2:
        current.next = head2
        head2 = head2.next
        current = current.next

    header = dummy.next
    return header
