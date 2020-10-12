'''
Write two Python functions to find the minimum number in a list. The first
function should compare each number to every other number on the list. 𝑂(𝑛2).
The second function should be linear 𝑂(𝑛).
'''

def minimum_in_list_quadratic(item_list):
    minimum = 0
    for l1 in item_list:
        for l2 in item_list:
            if l2 <= l1:
                minimum = l2    
    return minimum

def minimum_in_list_linear(item_list):
    minimum = item_list[0]
    for item in item_list:
        if item < minimum:
            minimum = item
    return minimum

# driver
item_list = [-20, 1, 0, 204, 123, -200]
print(f"Minium in list is: {minimum_in_list_quadratic(item_list)}")
print(f"Minimum in list is: {minimum_in_list_linear(item_list)}")