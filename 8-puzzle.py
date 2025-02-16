import tkinter as tk
from tkinter import ttk
import heapq
import random
from typing import List

class PuzzleState:
    def __init__(self, board, goal, g, h, parent=None):
        self.board = board
        self.goal = goal
        self.g = g
        self.h = h
        self.parent = parent
        self.empty_tile = self.find_empty_tile()

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def get_manhattan_distance(self):
        distance = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    value = self.board[i][j]
                    for x in range(3):
                        for y in range(3):
                            if goal_state[x][y] == value:
                                distance += abs(i - x) + abs(j - y)
        return distance

    def generate_neighbors(self):
        neighbors = []
        i, j = self.empty_tile
        moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for new_i, new_j in moves:
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                neighbor = PuzzleState(new_board, self.goal, self.g + 1, 0, self)
                neighbor.h = neighbor.get_manhattan_distance()
                neighbors.append(neighbor)
        return neighbors

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver")
        
        # Initialize puzzle state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.current_state = self.generate_random_puzzle()
        
        # Create and configure main frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create puzzle buttons
        self.buttons = []
        self.create_puzzle_grid()
        
        # Create control buttons
        self.create_controls()
        
        # Solution variables
        self.solution = None
        self.current_step = 0
        
        # Update initial display
        self.update_display()

    def get_inversions(self, board_1d):
        inversions = 0
        for i in range(len(board_1d)):
            for j in range(i + 1, len(board_1d)):
                if board_1d[i] != 0 and board_1d[j] != 0 and board_1d[i] > board_1d[j]:
                    inversions += 1
        return inversions

    def is_solvable(self, board):
        # Convert 2D board to 1D list
        board_1d = [num for row in board for num in row]
        inversions = self.get_inversions(board_1d)
        
        # For a 3x3 puzzle, if the blank is on an even row counting from the bottom, 
        # the number of inversions must be odd for the puzzle to be solvable.
        # If the blank is on an odd row, the number of inversions must be even.
        blank_row = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    blank_row = i
                    break
        
        blank_from_bottom = 2 - blank_row  # Convert to counting from bottom
        return (blank_from_bottom % 2 == 0 and inversions % 2 == 1) or \
               (blank_from_bottom % 2 == 1 and inversions % 2 == 0)

    def generate_random_puzzle(self):
        while True:
            # Create list of numbers 0-8
            numbers = list(range(9))
            # Shuffle the numbers
            random.shuffle(numbers)
            # Convert to 2D board
            board = [numbers[i:i + 3] for i in range(0, 9, 3)]
            
            # Check if puzzle is solvable
            if self.is_solvable(board):
                return board

    def create_puzzle_grid(self):
        puzzle_frame = ttk.Frame(self.main_frame)
        puzzle_frame.grid(row=0, column=0, padx=5, pady=5)
        
        style = ttk.Style()
        style.configure('Puzzle.TButton', font=('Helvetica', 20, 'bold'), width=3)
        
        for i in range(3):
            row = []
            for j in range(3):
                btn = ttk.Button(puzzle_frame, style='Puzzle.TButton')
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

    def create_controls(self):
        control_frame = ttk.Frame(self.main_frame)
        control_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(control_frame, text="New Puzzle", command=self.new_puzzle).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Solve", command=self.solve_puzzle).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="Next Step", command=self.next_step).grid(row=0, column=2, padx=5)
        
        self.status_label = ttk.Label(control_frame, text="")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=5)

    def new_puzzle(self):
        self.current_state = self.generate_random_puzzle()
        self.solution = None
        self.current_step = 0
        self.status_label["text"] = "New puzzle generated"
        self.update_display()

    def solve_puzzle(self):
        self.status_label["text"] = "Solving..."
        self.root.update()
        
        initial = PuzzleState(self.current_state, self.goal_state, 0, 0)
        initial.h = initial.get_manhattan_distance()
        
        open_list = []
        heapq.heappush(open_list, initial)
        closed_set = set()
        
        while open_list:
            current = heapq.heappop(open_list)
            current_tuple = tuple(map(tuple, current.board))
            
            if current.board == self.goal_state:
                path = []
                while current:
                    path.append(current.board)
                    current = current.parent
                path.reverse()
                
                self.solution = path
                self.current_step = 0
                self.status_label["text"] = f"Solution found! {len(path)} steps"
                self.update_display()
                return
            
            if current_tuple in closed_set:
                continue
                
            closed_set.add(current_tuple)
            
            for neighbor in current.generate_neighbors():
                neighbor_tuple = tuple(map(tuple, neighbor.board))
                if neighbor_tuple not in closed_set:
                    heapq.heappush(open_list, neighbor)
        
        self.status_label["text"] = "No solution found!"

    def next_step(self):
        if self.solution and self.current_step < len(self.solution) - 1:
            self.current_step += 1
            self.current_state = [row[:] for row in self.solution[self.current_step]]
            self.update_display()
            self.status_label["text"] = f"Step {self.current_step} of {len(self.solution)-1}"
        else:
            self.status_label["text"] = "No more steps!"

    def update_display(self):
        for i in range(3):
            for j in range(3):
                value = self.current_state[i][j]
                self.buttons[i][j]["text"] = str(value) if value != 0 else " "

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()