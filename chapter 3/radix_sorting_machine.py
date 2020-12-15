'''
Radix Sorting Machine

Implement a radix sorting machine. A radix sort for base 10 integers is a
mechanical sorting technique that utilizes a collection of bins, one main bin
and 10 digit bins. Each bin acts like a queue and maintains its values in the
order that they arrive. The algorithm begins by placing each number in the main
bin. Then it considers each value digit by digit. The first value is removed and
placed in a digit bin corresponding to the digit being considered. For example,
if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is
placed in digit bin 7. Once all the values are placed in the corresponding digit
bins, the values are collected from bin 0 to bin 9 and placed back in the main
bin. The process continues with the tens digit, the hundreds, and so on. After
the last digit is processed, the main bin contains the values in order.

Main Bin   -> [                    ]
Digit Bins ->  [][][][][][][][][][]

18 13 17 15 118

In the first pass, 18 & 118 will be in bin 8, 13 in bin 3, 17 in bin 7 and 15 in bin 5.
main bin ==> [13 15 17 18 118]

In the second pass, 13, 15, 17, 18 and 118 are placed in bin 1
main bin ==> [13 15 17 18 118 ]
'''

from queues import Queue

def radix_sort(unsorted_numbers):
    main_bin = Queue()
    digit_bins_list = []
    is_sorted = False

    # create digit bins
    for i in range(10):
        digit_bins_list.append(Queue())
    
    # initialize main bin
    for num in unsorted_numbers:
        main_bin.enqueue(num)

    # Make multiple passes on the input numbers by going through 1's, 10's ,
    # 100's etc position in the decimal values and place them in appropriate
    # digit bins.
    digit_position = 1
    while not is_sorted:
        digit_pos_complete_count = 0
        while not main_bin.is_empty():
            num = main_bin.dequeue()
            num_divide_pos = num // digit_position
            digit_bins_list[num_divide_pos % 10].enqueue(num)
        
            # when a number is divided by digit_position and the result is 0,
            # increment a counter value. This tells if a number has been
            # exhausted or not when it comes to sorting it.
            if num_divide_pos == 0:
                digit_pos_complete_count += 1

            # if the counter value set above matches the length of the input
            # numbers, sorting is completed.
            if digit_pos_complete_count == len(unsorted_numbers):
                is_sorted = True

        digit_position *= 10

        # After each pass, when all the numbers are slotted into the appropriate
        # digit bins, dequeue the numbers from all digit bins into the main bin.
        for i in range(10):
            while not digit_bins_list[i].is_empty():
                main_bin.enqueue(digit_bins_list[i].dequeue())
    
    return main_bin

# driver code
if __name__ == "__main__":
    unsorted_numbers = [456, 233, 898, 24, 1, 9, 90, 71, 54, 6]
    print("Unsorted numbers:", unsorted_numbers)
    print("Sorted numbers:", radix_sort(unsorted_numbers))
