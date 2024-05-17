from collections import deque

# Exercise 2

def is_palindrome(s):
    
    edit_s = s.lower().replace(" ", "")
    deq = deque(edit_s)
    while len(deq) > 1:
       if deq.pop() != deq.popleft():
        return "It`s not a polindrome"
       return "It`s a polindrome"
    
 
# print(is_palindrome("Te    nEt     "))
# print(is_palindrome("tenet"))
# print(is_palindrome("Do g   "))
