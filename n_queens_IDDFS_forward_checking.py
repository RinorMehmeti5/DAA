import time

def solve_n_queens(n):
    def can_place(pos, ocuppied_rows, col):
        for i in range(ocuppied_rows):
            if pos[i] == col or \
                pos[i] - i == col - ocuppied_rows or \
                pos[i] + i == col + ocuppied_rows:
                return False
        return True

    def place_queens(pos, ocuppied_rows, n, limit):
        if ocuppied_rows == n:
            solutions[0] += 1
            return
        elif ocuppied_rows == limit:
            return
        else:
            for col in range(n):
                if can_place(pos, ocuppied_rows, col):
                    pos[ocuppied_rows] = col
                    place_queens(pos, ocuppied_rows + 1, n, limit)

    solutions = [0]
    for limit in range(1, n + 1):
        place_queens([0]*n, 0, n, limit)
    return solutions[0]

if __name__ == "__main__":
    n = int(input("Enter the size of the board: "))
    start_time = time.time()
    total_solutions = solve_n_queens(n)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
    print(f"Total solutions: {total_solutions}")
