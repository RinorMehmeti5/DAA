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
    
      def rotate(solution):
        n = len(solution)
        rotated = [0] * n
        for i in range(n):
            rotated[solution[i]] = n - 1 - i
        return rotated

    solutions = []
    place_queens([], m, depth, MR)
    return solutions

def print_solutions(solutions, n):                              
    console_size = shutil.get_terminal_size()   # Get the console size

    for solution in solutions:
        for row in range(n):
            line = ""
            for col in range(n):
                if col == solution[row]:
                    line += "Q "
                else:
                    line += "* "
            padding = " " * ((console_size.columns - len(line)) // 2)
            print(padding + line)
        print("\n")
    message = "============KY RAST KA {} ZHGJIDHJE============".format(len(solutions))
    padding = " " * ((console_size.columns - len(message)) // 2)
    print(padding + message)

n = int(input("Shenoni numrin e dimensioneve te shahut (n*n): "))
m = int(input("Shenoni numrin e mbretereshave: "))
depth = int(input("Vleren per depth (Depth for DLS): "))
MR = input("A doni te perfshini zgjidhjet me pasqyrim dhe rotacion? (po/jo): ")
start_time = time.time() 
solutions = solve_n_queens(n, m, depth, MR)
end_time = time.time()
print_solutions(solutions, n)

execution_time_message = "Execution time for finding solutions: {} seconds".format(end_time - start_time)
console_size = shutil.get_terminal_size()
padding = " " * ((console_size.columns - len(execution_time_message)) // 2)
print(padding + execution_time_message)
