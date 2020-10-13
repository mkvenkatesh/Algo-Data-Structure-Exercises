'''
One string is an anagram of another if the second is simply a rearrangement of
the first. For example, 'heart' and 'earth' are anagrams. The strings 'python'
and 'typhon' are anagrams as well. For the sake of simplicity, we will assume
that the two strings in question are of equal length and that they are made up
of symbols from the set of 26 lowercase alphabetic characters. Our goal is to
write a boolean function that will take two strings and return whether they are
anagrams.

# Algo 1 - O(n) + O(n)/ space O(S1)
# pass over str 1 into a dict with chars as keys and occurrences as values
# pass over str 2 and for every char you see as key, reduce the occurrence and
# if dict is empty at the end, the strings are anagrams

# Algo 2 - O(n^2)
Loop str1 and for each str1 char, check if it exist in str2. If it does, delete
that char from str2 and proceed. If it's not, break and return False

# Algo 3 - O(nlogn)
Sort both the strings and run a loop to compare.
'''

# O(n^2)
def is_anagram_sol1(str1, str2):
    str2 = list(str2)
    for char in str1:
        if char in str2:
            str2.remove(char)
        else:
            return False
    if not str2:
        return True

print(is_anagram_sol1("heart", "earth"))
print(is_anagram_sol1("python", "typhon"))
print(is_anagram_sol1("python", "earth"))

# O(nlogn)
def is_anagram_sol2(str1, str2):
    return sorted(str1) == sorted(str2)

print()
print(is_anagram_sol2("heart", "earth"))
print(is_anagram_sol2("python", "typhon"))
print(is_anagram_sol2("python", "earth"))


# Time - O(n) / Space - O(s1)
def is_anagram_sol3(str1, str2):
    counts_hash = {}
    for char in str1:
        if char not in counts_hash:
            counts_hash[char] = 0
        counts_hash[char] += 1

    for char in str2:
        if char in counts_hash:
            counts_hash[char] -= 1
            if counts_hash[char] == 0:
                del counts_hash[char]
        else:
            return False

    return True

print()
print(is_anagram_sol3("heart", "earth"))
print(is_anagram_sol3("python", "typhon"))
print(is_anagram_sol3("python", "earth"))