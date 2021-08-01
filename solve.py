import os
import time
import grid
import sudoku
import sys
sys.setrecursionlimit(50000)

multi_choices = []


def solve(sudoku_array, i):

    if 0 in sudoku_array and i < 81:
        possible_values = []
        if i not in sudoku.locked_values:
            for possible_digit in range(1, 10):
                if possible_digit not in sudoku.get_used_values(i):
                    possible_values.append(possible_digit)
                    sudoku_array[i] = possible_values[0]
            if len(possible_values) > 1:
                multi_choices.append([i, possible_values])
            if len(possible_values) == 0:
                last_multi_choice = multi_choices[len(multi_choices)-1]
                last_multi_choice[1].pop(0)
                sudoku_array = reset_digits(
                    sudoku_array, last_multi_choice[0]+1)
                sudoku_array[last_multi_choice[0]] = last_multi_choice[1][0]
                if len(last_multi_choice[1]) < 2:
                    multi_choices.pop()
                solve(sudoku_array, last_multi_choice[0]+1)
        grid.to_grid(sudoku_array)
        time.sleep(0.005)
        os.system('clear')
        if 0 in sudoku_array and i < 81:
            solve(sudoku_array, i+1)
        else:
            finished(sudoku_array)
            return True


def finished(sudoku_array):
    os.system("clear")
    grid.to_grid(sudoku_array)
    print("done ")


def reset_digits(sudoku_array, loc):
    for i in range(loc, 80):
        if i not in sudoku.locked_values:
            sudoku_array[i] = 0
    return sudoku_array


solve(sudoku.sudoku_array, 0)
