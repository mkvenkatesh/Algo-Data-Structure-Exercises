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
This solution only implements five simple rules in solving a sudoku puzzle so it
should solve most of the "easy" or "medium" category of Sudoku. The rules are
listed here: http://www.sudokusnake.com/techniques.php

Rules used in this solution:
    * Hidden singles by box
    * Hidden singles
    * Naked singles
    * Pointing
    * Claiming

"""

import sys

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


def build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array):
    candidates_nums = []
    candidates_pos = {}
    for idx_3x3 in range(len(nums_3x3)):
        candidates_nums.append({})
        for num in range(1, 10):
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
                            if ((i,j) in eliminate_candidate_array and num in eliminate_candidate_array[(i,j)]):
                                continue
                            candidates_nums[idx_3x3][num].append((i, j))
                            if (i,j) not in candidates_pos:
                                candidates_pos[(i,j)] = []
                            candidates_pos[(i,j)].append(num)

    return candidates_nums, candidates_pos

def validate_solution(nums_rows, nums_cols, nums_3x3):
    for check_num in range(1, 10):
        for idx_input in range(9):
            if (check_num not in nums_rows[idx_input]) or ((check_num not in nums_cols[idx_input])) or (check_num not in nums_3x3[idx_input]):
                return False
    return True

def sudoku_solver(input):

    passes = 0
    prev_pass_cnt = -1
    eliminate_candidate_array = {}

    # get numbers in each row/col/local 3x3 block
    nums_rows, nums_cols, nums_3x3 = build_helper_arrays()

    # Find the candidates for each number in a 3x3 grid and all possible number
    # candidates for a given open position
    candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)

    # print(candidates_nums)
    # print()
    # print(candidates_pos)
    # print()

    # Eliminate and ensure the best position for a given number and position
    # using the following rules:

    while True:
        # 1. Hidden singles by box - if there's only one number candidate for a
        #    position, set that number to that position. This can be obtained from
        #    candidate_num array of length 1
        continue_block = True
        while continue_block:
            continue_block = False
            for idx_3x3 in range(len(candidates_nums)):
                for num in candidates_nums[idx_3x3]:
                    if len(candidates_nums[idx_3x3][num]) == 1:
                        continue_block = True
                        
                        cell_row = candidates_nums[idx_3x3][num][0][0]
                        cell_col = candidates_nums[idx_3x3][num][0][1]
                        input[cell_row][cell_col] = num
                        
                        # maintain num* arrays
                        nums_rows[cell_row].append(num)
                        nums_cols[cell_col].append(num)
                        nums_3x3[idx_3x3].append(num)
                        passes += 1
                        print(f"Pass {passes}: Hidden Singles by Box")

            candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)
        
        # 2. Hidden singles - if there's only one number candidate for a given row
        #    or column. This can be obtained from candidate_pos dictionary. Loop
        #    through and get all the keys that start with a row or column and see if
        #    there's any num that's only in one position, if so, set that for that
        #    position
        #       (6, 1): [1, 6, 8], 
        #       (6, 2): [1, 2, 5, 6, 7, 8], 
        #       (6, 3): [1, 2, 5], 
        #       (6, 4): [1, 2, 5, 8], 
        #       (6, 5): [5, 8], 
        #       (6, 7): [2, 5, 8], 
        #    after cancelling all the repeated numbers in each position, you are
        #    left only with 7. So set 7 in (6,2)
        while True:
            hidden_single_candidates = {}
            for idx in range(10):
                row_lvl_nums = {}
                col_lvl_nums = {}
                for pos in candidates_pos.keys():
                    # row
                    if idx == pos[0]:
                        for v in candidates_pos[pos]:
                            if v not in row_lvl_nums:
                                row_lvl_nums[v] = [0, pos]
                            row_lvl_nums[v][0] += 1
                    # col
                    if idx == pos[1]:
                        for v in candidates_pos[pos]:
                            if v not in col_lvl_nums:
                                col_lvl_nums[v] = [0, pos]
                            col_lvl_nums[v][0] += 1

                # if the row_lvl_nums or col_lvl_nums has a number with only one
                # occurrence, build a dictionary with the key as the position and value
                # as the number that should be set in that position
                for key, val in row_lvl_nums.items():
                    if val[0] == 1:
                        hidden_single_candidates[val[1]] = key
                        break
                for key, val in col_lvl_nums.items():
                    if val[0] == 1:
                        hidden_single_candidates[val[1]] = key
                        break

            # if there's no candidates, break out of the loop
            if hidden_single_candidates == {}:
                break
            
            for key, val in hidden_single_candidates.items():            
                input[key[0]][key[1]] = val                    
                # maintain num* arrays
                nums_rows[key[0]].append(val)
                nums_cols[key[1]].append(val)
                nums_3x3[(3 * (key[0] // 3)) + (key[1] // 3)].append(val)
                passes += 1
                print(f"Pass {passes}: Hidden Singles")

            candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)
        
        # 3. Naked single - if a number shows up as the only candidate in a cell in
        #    a 3x3 grid. This can be obtained from candidate_num array by looking at
        #    each 3x3 grid and finding if after cancelling all the common
        #    occurrences of the positions for the nums, there exists only one num
        #    with one position.
        #       8: [(6,1), (7,2)]
        #       9: [(6,1), (7,2)]
        #       4: [(6,1), (7,3)]
        #    after cancelling all the position occurrences, you are left with 4
        #    number with a position of 7,3, so set 4 in (7,3)
        while True:
            naked_singles_candidates = {}
            for idx_3x3 in range(len(candidates_nums)):
                naked_singles_temp = {}
                for k, v in candidates_nums[idx_3x3].items():
                    for pos in v:
                        if pos not in naked_singles_temp:
                            naked_singles_temp[pos] = [0, k]
                        naked_singles_temp[pos][0] += 1
                for k, v in naked_singles_temp.items():
                    if v[0] == 1:
                        naked_singles_candidates[k] = v[1]    

            # if there's no candidates, break out of the loop
            if naked_singles_candidates == {}:
                break

            for key, val in naked_singles_candidates.items():            
                input[key[0]][key[1]] = val                    
                # maintain num* arrays
                nums_rows[key[0]].append(val)
                nums_cols[key[1]].append(val)
                nums_3x3[(3 * (key[0] // 3)) + (key[1] // 3)].append(val)
                passes += 1
                print(f"Pass {passes}: Naked Singles")

            candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)

        # 4. Pointing -  If the only instances of a candidate within a box are in
        #    the same row or column, you can eliminate candidates of that value from
        #    any other cell in the respective row or column. This can be obtained by
        #    looking at candidate_num array to see if each 3x3 grid has the same row
        #    or column position present for a given number. if there is, eliminate
        #    that number from candidate_pos array for that row or column
        #       3x3_1 => 5: [(0, 4), (1, 4)]
        #       3x3_3 => 5: [(3,4)]
        #       (0, 4): [3, 4, 5, 7, 9], 
        #       (1, 4): [3, 5, 7], 
        #       (2, 4): [3, 4, 7, 9], 
        #       (3, 4): [1, 4, 5, 7, 8, 9], 
        #    5 is on column 4, so we can eliminate 5 from other 3x3 grids that has 5
        #    in it (for e.g (3,4))
        
        # check in candidate_nums for row/col and see if they are the same for a
        # given num. if it's the same, get that same row/col number and look in
        # candidate_pos for all positions that match that row/col with the matching
        # number and add them to eliminate_candidate_array

        for idx_3x3 in range(len(candidates_nums)):
            for k,v in candidates_nums[idx_3x3].items():
                same_row_col_dict = {}
                same_row_col_record = ()
                # find if the num is on the same row or columns in its candidate
                # position in the current 3x3 grid
                for pos in v:
                    if (0, pos[0]) not in same_row_col_dict:
                        same_row_col_dict[(0, pos[0])] = 0
                    same_row_col_dict[(0, pos[0])] += 1
                    if (1, pos[1]) not in same_row_col_dict:
                        same_row_col_dict[(1, pos[1])] = 0
                    same_row_col_dict[(1, pos[1])] += 1
                for pos, cnt in same_row_col_dict.items():
                    if cnt == len(v):
                        same_row_col_record = pos
                        break
                # match the row/col obtained from above to match with candidate_pos
                # for all pos that has the matched row/col, eliminating the pos from
                # candidate_num and adding the rest of the pos from candidate_pos
                # for that num to the eliminate_candidate list
                if same_row_col_record != ():
                    for pos in candidates_pos:
                        if pos[same_row_col_record[0]] == same_row_col_record[1]:
                            if (pos not in v) and (k in candidates_pos[pos]):
                                if pos not in eliminate_candidate_array:
                                    eliminate_candidate_array[pos] = []
                                eliminate_candidate_array[pos].append(k)
                                print(f"Pointing: Candidate {k} eliminated from position {pos}")

        candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)

        # 5. Claiming - If the only instances of a candidate within a row or column
        #    are in the same box, you can eliminate candidates of that value from
        #    any other cell in the box. This can be obtained by looking at
        #    candidate_pos array first for a given row or column and seeing if a
        #    number appears only in one 3x3 grid. If so, eliminate the number
        #    appearance in all other cells in that 3x3 grid.

        # for each row or col in candidate_pos, get the numbers that are only in one
        # 3x3 grid. Note down that number and grid position. Based on grid position,
        # go to candidate_nums and get all the positions for the matches nums, note
        # down all the positions for that num that doesn't have the matched row/col.
        # Eliminate that num/pos from candidates.
        for seq in [0, 1]: #0 is row, 1 is col
            for idx_row_col in range(9):
                row_col_cpos = {}
                for pos in candidates_pos:
                    idx_3x3 = (3 * (pos[0] // 3)) + (pos[1] // 3)
                    if pos[seq] == idx_row_col:
                        if idx_3x3 not in row_col_cpos:
                            row_col_cpos[idx_3x3] = set()
                        row_col_cpos[idx_3x3] = row_col_cpos[idx_3x3] | set(candidates_pos[pos])

                # We have a dictionary now for a given row/col of the 3x3 grid index
                # and the candidates it has. Loop from 1..9 and see if the numbers
                # are in only one grid. If so, check that grid for that num and
                # exclude all positions that match with the current row/col
                for num in range(1, 10):
                    temp_cnt = 0
                    last_seen_idx_3x3 = -1
                    for k, v in row_col_cpos.items():
                        if num in v:
                            temp_cnt += 1
                            last_seen_idx_3x3 = k
                        if temp_cnt > 1:
                            last_seen_idx_3x3 = -1
                    # if there's a num which is only in one 3x3 grid        
                    if last_seen_idx_3x3 != -1:
                        for pos in candidates_nums[last_seen_idx_3x3][num]:
                            if pos[seq] != idx_row_col:
                                if pos not in eliminate_candidate_array:
                                    eliminate_candidate_array[pos] = []
                                if num not in eliminate_candidate_array[pos]:
                                    eliminate_candidate_array[pos].append(num)
                                    print(f"Claiming: Candidate {num} eliminated from position {pos}")
        
            candidates_nums, candidates_pos = build_num_candidates(nums_rows, nums_cols, nums_3x3, eliminate_candidate_array)

        if prev_pass_cnt == passes:
            break

        prev_pass_cnt = passes

    
    solved = validate_solution(nums_rows, nums_cols, nums_3x3)
    if solved:
        print("\nSudoku puzzle solved!\n")
    else:
        print("\nSudoku puzzle solved incorrectly or unsolved!\n")

# input = [
#     [6, 0, 0, 0, 0, 0, 3, 2, 0],
#     [0, 5, 0, 0, 7, 0, 4, 1, 0],
#     [0, 0, 1, 0, 8, 5, 0, 0, 7],
#     [0, 2, 0, 7, 0, 9, 1, 5, 3],
#     [0, 1, 0, 0, 0, 0, 0, 7, 0],
#     [7, 9, 4, 1, 0, 3, 0, 8, 0],
#     [1, 0, 0, 8, 2, 0, 7, 0, 0],
#     [0, 6, 2, 0, 9, 0, 0, 3, 0],
#     [0, 7, 8, 0, 0, 0, 0, 0, 2]
# ]

input = [
    [0, 0, 0, 0, 6, 0, 0, 0, 4],
    [3, 9, 0, 0, 0, 0, 1, 0, 0],
    [7, 0, 4, 3, 0, 0, 0, 0, 6],
    [0, 0, 3, 1, 0, 4, 0, 0, 0],
    [0, 1, 0, 6, 7, 9, 0, 4, 0],
    [0, 0, 0, 2, 0, 3, 7, 0, 0],
    [4, 0, 0, 0, 0, 5, 9, 0, 3],
    [0, 0, 5, 0, 0, 0, 0, 8, 2],
    [2, 0, 0, 0, 3, 0, 0, 0, 0]
]


# input = [
#     [0, 0, 0, 8, 0, 2, 0, 0, 1],
#     [0, 9, 0, 6, 0, 1, 0, 4, 0],
#     [5, 0, 0, 0, 0, 0, 0, 0, 6],
#     [0, 2, 3, 0, 0, 0, 8, 6, 0],
#     [8, 7, 0, 0, 6, 0, 0, 9, 2],
#     [6, 5, 9, 0, 0, 0, 1, 7, 0],
#     [3, 0, 0, 0, 0, 0, 4, 0, 9],
#     [0, 4, 0, 7, 0, 3, 6, 1, 0],
#     [0, 0, 0, 4, 0, 6, 0, 0, 0]
# ]


# input = [
#     [0, 0, 4, 0, 0, 0, 2, 1, 3],
#     [2, 0, 1, 3, 0, 0, 0, 0, 9],
#     [0, 3, 0, 0, 0, 2, 4, 7, 0],
#     [0, 2, 0, 0, 6, 0, 7, 0, 0],
#     [0, 0, 0, 0, 0, 8, 0, 0, 1],
#     [0, 5, 0, 0, 0, 0, 0, 3, 0],
#     [6, 0, 0, 2, 0, 0, 0, 9, 0],
#     [0, 0, 2, 5, 0, 0, 0, 6, 0],
#     [0, 0, 5, 6, 9, 1, 0, 0, 0]
# ]

sudoku_solver(input)

for idx in range(len(input)):
    for val in input[idx]:
        print(val, end="  ")
    print()

    