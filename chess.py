import time
import os
import shutil

def solve_n_queens(n, m, depth, MR):
    def can_place(pos, ocuppied_rows, n):
        for i in range(ocuppied_rows):
            if pos[i] == pos[ocuppied_rows] or \
                    pos[i] - i == pos[ocuppied_rows] - ocuppied_rows or \
                    pos[i] + i == pos[ocuppied_rows] + ocuppied_rows:
                return False
        return True

    def place_queens(pos, target, depth, MR):
        row = len(pos)
        if depth >= 0 and target == 0:
            if MR == "po":
                solutions.append(pos[:])
            else:
                if not is_duplicate(pos, solutions):
                    solutions.append(pos[:])
        elif depth >= 0:
            for col in range(n):
                pos.append(col)
                if can_place(pos, row, n):
                    place_queens(pos, target - 1, depth - 1, MR)
                pos.pop()

    def is_duplicate(new_solution, existing_solutions):
        for old_solution in existing_solutions:
            if old_solution in generate_transforms(new_solution):
                return True
        return False

    def generate_transforms(solution):
        transforms = [solution]                 # original
        transforms.append(solution[::-1])       # vertical reflection
        for _ in range(3):
            solution = rotate(solution)
            transforms.append(solution)         # rotation
            transforms.append(solution[::-1])   # vertical reflection
        return transforms
