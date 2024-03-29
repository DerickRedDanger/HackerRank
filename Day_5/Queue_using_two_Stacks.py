"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


"""
Queue are a first in first out structure, so the element at the front of the list is the first to be processed
Queue using two stacks, means using two stacks (last in, first out. So last element is the first processed), as if they were a single queue.
that is done because poping a element that isn't the last from a list, forces python to reorganize the whole list,
moving the elements after that element foward. This can be computationally costly as the list increase in size.

That's why we are using two stacks instead. we will keep appending elements to the first stack, keeping them in order.
But when we need to dequeue elements, if S2 is already empty, we will pop elements from the first list and append them in the second list,
So that the first element in the first list become the last in the second one, allowing us to simply pop them in order.
If s2 is not empty, then we can just continue to pop it's last element, only adding elements from S1 when it's empty again.
"""

# Each time input is called, another line of input is sent.
n = int(input())
s1 = []
s2 = []
for _ in range(n):
    queries = input().split()
    if queries[0] == "1":
        s1.append(queries[1])
        
    elif queries[0] == "2":
        if not s2:
            for _ in range(len(s1)):
                s2.append(s1.pop())
        s2.pop()
        
    elif queries[0] =="3":
        if s2:
            print(s2[-1])
        else:
            print(s1[0])
        