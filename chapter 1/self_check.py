"""
Self Check 

Here is a self check that really covers everything so far. You may have heard of
the infinite monkey theorem? The theorem states that a monkey hitting keys at
random on a typewriter keyboard for an infinite amount of time will almost
surely type a given text, such as the complete works of William Shakespeare.
Well, suppose we replace a monkey with a Python function. How long do you think
it would take for a Python function to generate just one sentence of
Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

The way we will simulate this is to write a function that generates a string
that is 27 characters long by choosing random letters from the 26 letters in the
alphabet plus the space. We will write another function that will score each
generated string by comparing the randomly generated string to the goal. 

A third function will repeatedly call generate and score, then if 100% of the
letters are correct we are done. If the letters are not correct then we will
generate a whole new string. To make it easier to follow your program’s progress
this third function should print out the best string generated so far and its
score every 1000 tries.
"""

import random

def generate_random_string(length):
    random_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for i in range(length):
        random_letter_idx = random.randint(0, len(alphabet) - 1)
        random_string += alphabet[random_letter_idx]
    return random_string


def score_random_string(input, random_string):
    match_count = 0
    for i in range(len(input)):
        if input[i] == random_string[i]:
            match_count += 1    
    return int((match_count/len(input)) * 100) # return score as a % from 0-100


def infinite_monkey(input, tries):    
    best_score = 0
    best_string = ""
    for i in range(tries):
        random_string = generate_random_string(len(input))
        score = score_random_string(input, random_string)        
        if score > best_score:
            best_score = score
            best_string = random_string
    
    return (best_score, best_string)


if __name__ == "__main__":
    input = "methinks it is like a weasel"
    tries = 1000
    best_score, best_string = infinite_monkey(input, tries)
    print(f"Best score for randomly generated string in {tries} tries is: {best_score}%")
    print(f"Input is : {input}")
    print(f"Output is: {best_string}")
    

