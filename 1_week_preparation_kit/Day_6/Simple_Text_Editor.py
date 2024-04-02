"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Each time input is called, another line of input is sent.
N = int(input())
s = ""
last=[]
for i in range(N):
    queries = input().split()
    if queries[0] == "1":
        last.append(s)
        s += queries[1]
    elif queries[0] == "2":
        last.append(s)
        s = s[:len(s)-int(queries[1])]
    elif queries[0] =="3":
        print(s[int(queries[1])-1])
    elif queries[0] == "4":
        s=last.pop()