import time
import itertools
import grid
import os
import sys
sys.setrecursionlimit(5000)
sudoku_array = []

# Step1: Get full sudoku array from sudoku string input:
#number_suite = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
number_suite = input("Please input sudoku string here -->   ")
for digit in number_suite:
    sudoku_array.append(int(digit))

locked_values = []
for i in range(len(sudoku_array)-1):
    if sudoku_array[i] != 0:
        locked_values.append(i)

# Step2: sudoku array to lines and grids logic:


def get_vertical_line(line):
    line_array = []
    for i in range(9):
        line_array.append(sudoku_array[i*9+line])

    return line_array


def get_horizontal_line(line):
    line_array = []
    for i in range(9):
        line_array.append(sudoku_array[9*line+i])

    return line_array


def array_loc_to_iloc(array_loc):
    num = array_loc+1
    vertical_loc = int((num)/9)+1 if num > 9 else 1
    vertical_loc = vertical_loc-1 if num % 9 == 0 else vertical_loc
    vertical_loc = vertical_loc-1 if vertical_loc > 0 else vertical_loc
    horizontal_loc = num % 9 if num > 9 else num
    horizontal_loc = 9 if num % 9 == 0 else horizontal_loc
    horizontal_loc -= 1

    return[horizontal_loc, vertical_loc]


def iloc_to_array_loc(iloc):
    array_loc = iloc[1]*9+iloc[0]

    return array_loc


# Step3: get a grid ilocs from grid number:
grid_starts = {
    0: 0,
    1: 3,
    2: 6,
    3: 27,
    4: 30,
    5: 33,
    6: 54,
    7: 57,
    8: 60
}


def grid_to_grid_ilocs(grid_number):
    grid_ilocs_array = []
    grid_start_array_loc = grid_starts[grid_number]
    grid_start_iloc = array_loc_to_iloc(grid_start_array_loc)
    for horizontal_loc in range(3):
        for vertical_loc in range(3):
            grid_ilocs_array.append(
                [grid_start_iloc[0]+horizontal_loc, grid_start_iloc[1]+vertical_loc])
    return grid_ilocs_array


# grid_to_grid_ilocs(4)

# step4: get a grid number from an iloc:


def iloc_to_grid_number(iloc):
    for grid_number in range(9):
        if iloc in grid_to_grid_ilocs(grid_number):
            return grid_number


def grid_ilocs_to_grid_array_locs(grid_ilocs_array):
    grid_array_locs = []
    for iloc in grid_ilocs_array:
        grid_array_locs.append(iloc_to_array_loc(iloc))
    return sorted(grid_array_locs)


def grid_array_locs_to_values(grid_array_locs):
    grid_values = []
    for loc in grid_array_locs:
        grid_values.append(sudoku_array[loc])

    return grid_values


def array_loc_to_grid_values(array_loc):
    iloc = array_loc_to_iloc(array_loc)
    grid_number = iloc_to_grid_number(iloc)
    grid_ilocs = grid_to_grid_ilocs(grid_number)
    grid_array_locs = grid_ilocs_to_grid_array_locs(grid_ilocs)
    grid_values = grid_array_locs_to_values(grid_array_locs)

    return grid_values


def get_used_values(array_loc):
    grid_values = array_loc_to_grid_values(array_loc)
    iloc = array_loc_to_iloc(array_loc)
    horizontal_values = get_horizontal_line(iloc[1])
    vertical_values = get_vertical_line(iloc[0])
    all_used_values = set(itertools.chain(
        grid_values, horizontal_values, vertical_values))

    return all_used_values
