"""
Given a sudoku grid with some numbers filled in, complete the grid with the
rules of sudoku

It's a 9 x 9 grid, so use a 9x9 matrix.
Program takes a 9x9 matrix with some numbers filled in
Fill out the matrix with the following rules
    * In a horizontal row, there should be only one instance of numbers 1 to 9
    * In a vertical row, there should be only one instance of numbers 1 to 9
    * In a 3x3 smaller grid, there should be only one instance of numbers 1 to 9

Solution Notes:
This solution only implements two basic rules in solving a sudoku puzzle so it
should solve most of the "easy" category of Sudoku

Algorithm:

"""

def build_helper_arrays():
    nums_rows = []
    nums_cols = []
    nums_3x3 = []

    for i in range(len(input)):                            
        nums_rows.append([])
        nums_cols.append([])   

        temp_col_arr = []
        for j in range(len(input)):
            temp_col_arr.append(input[j][i])

            # numbers in local 3x3 grid
            if i % 3 == 0 and j % 3 == 0:
                nums_3x3.append([])
            if input[i][j] != 0:
                nums_3x3[(3 * (i // 3)) + (j // 3)].append(input[i][j])

        for num in range(1, 10):
            # numbers in each row
            if num in input[i]:
                nums_rows[i].append(num)
            
            # numbers in each col
            if num in temp_col_arr:
                nums_cols[i].append(num)

    return nums_rows, nums_cols, nums_3x3

def sudoku_solver(input):

    # get numbers in each row/col/local 3x3 block
    nums_rows, nums_cols, nums_3x3 = build_helper_arrays()

    # Find the candidates for each open position on the board
    empty_candidates_count = 0
    while empty_candidates_count != 9:
        candidates_nums = []
        empty_candidates_count = 0
        # loop through each 3x3 grid
        for idx_3x3 in range(len(nums_3x3)):
            candidates_nums.append({})
            for num in range(1, 10):
                # find the best position(s) for a given num with the following
                # constraints
                # a) make sure num is not in 3x3 grid
                # b) in the 3x3 grid, eliminate rows and cols that has the num
                # in the corresponding row or column and use this information to
                # build the best candidate positions for num
                # c) if in a given horizontal, vertical or 3x3 grid, there are
                # nums with same candidates, the occurrence of that candidate
                # can be eliminated from the row, column or the grid in other
                # cells.
                # d) if a num appears only in 2 or 3 adjacent cells in a row or
                # column, that num can be eliminated from other cells in the
                # local 3x3 grid
                if num not in nums_3x3[idx_3x3]: 
                    if num not in candidates_nums[idx_3x3]:               
                        candidates_nums[idx_3x3][num] = []
                    
                    # gather row candidate for local grid for the given num
                    row_start_3x3 = 3 * (idx_3x3 // 3)                
                    row_3x3_cds = []
                    for row_3x3_idx in range(row_start_3x3, row_start_3x3 + 3):
                        if num not in nums_rows[row_3x3_idx]:
                            row_3x3_cds.append(row_3x3_idx)
                    
                    # gather col candidate for local grid for the given num
                    col_start_3x3 = 3 * (idx_3x3 % 3)                
                    col_3x3_cds = []
                    for col_3x3_idx in range(col_start_3x3, col_start_3x3 + 3):
                        if num not in nums_cols[col_3x3_idx]:
                            col_3x3_cds.append(col_3x3_idx)                    
                    
                    # find all candidate position for a given num and store it in Candidate array
                    for i in row_3x3_cds:
                        for j in col_3x3_cds:
                            if input[i][j] == 0:                                
                                candidates_nums[idx_3x3][num].append((i, j))                    
                    
                    # if there's only one candidate for num, set that num on that
                    # candidate position
                    if len(candidates_nums[idx_3x3][num]) == 1:
                        cell_row = candidates_nums[idx_3x3][num][0][0]
                        cell_col = candidates_nums[idx_3x3][num][0][1]
                        input[cell_row][cell_col] = num
                        
                        # make sure to add num to the three arrays we maintain -
                        # num_rows, num_cols and num_3x3
                        nums_rows[cell_row].append(num)
                        nums_cols[cell_col].append(num)
                        nums_3x3[idx_3x3].append(num)

                        # remove references to candidate positions
                        del candidates_nums[idx_3x3][num]
                        for key in candidates_nums[idx_3x3]:
                            if (cell_row, cell_col) in candidates_nums[idx_3x3][key]:
                                candidates_nums[idx_3x3][key].remove((cell_row, cell_col))

            if candidates_nums[idx_3x3] == {}:
                empty_candidates_count += 1

input = [
    [6, 0, 0, 0, 0, 0, 3, 2, 0],
    [0, 5, 0, 0, 7, 0, 4, 1, 0],
    [0, 0, 1, 0, 8, 5, 0, 0, 7],
    [0, 2, 0, 7, 0, 9, 1, 5, 3],
    [0, 1, 0, 0, 0, 0, 0, 7, 0],
    [7, 9, 4, 1, 0, 3, 0, 8, 0],
    [1, 0, 0, 8, 2, 0, 7, 0, 0],
    [0, 6, 2, 0, 9, 0, 0, 3, 0],
    [0, 7, 8, 0, 0, 0, 0, 0, 2]
]

# input = [
#     [0, 8, 0, 9, 4, 0, 0, 5, 0],
#     [0, 0, 0, 0, 0, 3, 0, 0, 0],
#     [7, 0, 5, 0, 1, 0, 0, 0, 0],
#     [8, 0, 0, 0, 2, 0, 0, 0, 3],
#     [9, 0, 7, 0, 0, 0, 2, 0, 8],
#     [2, 0, 0, 0, 7, 0, 0, 0, 1],
#     [0, 0, 0, 0, 9, 0, 8, 0, 4],
#     [0, 0, 0, 5, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 3, 2, 0, 7, 0]
# ]

sudoku_solver(input)

for idx in range(len(input)):
    for val in input[idx]:
        print(val, end="  ")
    print()