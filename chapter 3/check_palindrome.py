'''
Palindrome Checker using Deque

The solution to this problem will use a deque to store the characters of the
string. We will process the string from left to right and add each character to
the rear of the deque. At this point, the deque will be acting very much like an
ordinary queue. However, we can now make use of the dual functionality of the
deque. The front of the deque will hold the first character of the string and
the rear of the deque will hold the last character

Since we can remove both of them directly, we can compare them and continue only
if they match. If we can keep matching first and the last items, we will
eventually either run out of characters or be left with a deque of size 1
depending on whether the length of the original string was even or odd. In
either case, the string must be a palindrome.

'''

from deque import Deque

def palindrome_checker(word):
    if len(word) == 0:
        raise ValueError("Input string is empty. Input should have at least one character.")

    d = Deque()
    for char in word:
        d.add_rear(char)

    while True:
        if d.is_empty() or d.size() == 1:
            return True
        elif d.remove_front() == d.remove_rear():
            continue
        else:
            return False
    
if __name__ == "__main__":
    input_str = [" madam", "intercodes ", " toot ", "tt", "a"]
    for word in input_str:
        # remove whitespace from beginning and end of string
        word = word.strip()
        print(word, "is a palindrome?", palindrome_checker(word))