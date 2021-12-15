# export SESSION_COOKIE="53616c7465645f5f00ce5818b9a09d593c0322cb2fe763039ec33d9799ebfa249737e59e910a20ad74c21ac6ec083202"

from aoc_utils import aoc_utils
import os

year = 2021
puzzle = 14

problem_input = aoc_utils.fetch_and_save(year, puzzle)
os.rename("input.txt", f"Day{puzzle}/input{puzzle}")
os.rename("problem.txt", f"Day{puzzle}/problem{puzzle}.txt")

print(problem_input)
