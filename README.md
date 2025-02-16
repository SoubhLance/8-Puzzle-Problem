# 8-Puzzle Problem Solver

Welcome to the **8-Puzzle Problem Solver**! This project is an interactive GUI-based application that solves the classic 8-puzzle problem using the A* search algorithm with Manhattan distance as the heuristic. The goal is to rearrange the tiles of the puzzle to match the target goal state.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)

## Overview

The **8-Puzzle Problem Solver** is a graphical application developed using Python's `Tkinter` library. It allows users to generate a random puzzle, solve the puzzle using the A* algorithm, and view the step-by-step solution. The Manhattan distance heuristic is used to guide the search process in finding the optimal solution.

## Features

- Random puzzle generation that ensures the puzzle is solvable.
- A* algorithm implementation to solve the puzzle.
- Step-by-step solution visualization.
- Easy-to-use graphical user interface (GUI) built with `Tkinter`.
  
## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your machine.
- Required Python libraries:
  - `Tkinter` (usually comes pre-installed with Python).
  - `heapq` (built-in Python library).

## Screenshots

  ![Screenshot 2025-02-16 211512](https://github.com/user-attachments/assets/13a49a66-008d-4322-a628-c1cd629d3dde)
  ![Screenshot 2025-02-16 211520](https://github.com/user-attachments/assets/5023e684-2f73-4067-842b-5888756b1b03)
  ![Screenshot 2025-02-16 211547](https://github.com/user-attachments/assets/dc92db03-4a61-477b-bf8f-2a8e9f780776)
  
_Screenshot: Example of the puzzle solver interface in action._

## Installation

To install and run the 8-Puzzle Problem Solver locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/SoubhLance/8-Puzzle-Problem.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 8-Puzzle-Problem
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required libraries (if not already installed):
    ```bash
    pip install tkinter
    ```

5. Run the application:
    ```bash
    python puzzle_gui.py
    ```

## Usage

1. Launch the application to see the initial puzzle grid.
2. Click **New Puzzle** to generate a random, solvable puzzle.
3. Click **Solve** to use the A* algorithm to find a solution.
4. After solving, click **Next Step** to view the solution step-by-step.
5. The status bar will show the progress and total number of steps to solve the puzzle.

### Puzzle State Representation

The puzzle consists of a 3x3 grid where each tile contains a number between 1 and 8, and one tile is empty (represented as 0). The goal of the puzzle is to arrange the numbers in ascending order, with the empty tile in the bottom-right corner.

### A* Search Algorithm

This application uses the A* algorithm with the Manhattan distance as the heuristic to guide the search process and find the optimal solution. The algorithm explores neighboring states and ranks them based on their cost (`g` value) and heuristic (`h` value).

## Technologies

- **Python 3.x**: Main programming language used to develop the project.
- **Tkinter**: Library used for creating the graphical user interface (GUI).
- **A* Algorithm**: Used for solving the puzzle efficiently.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to the project owner:

**Soubhik Sadhu**  
- GitHub: [SoubhLance](https://github.com/SoubhLance)
- LinkedIn: [Soubhik Sadhu](https://www.linkedin.com/in/soubhiksadhu)
- Email: [studysadhu2022@gmail.com](mailto:studysadhu2022@gmail.com)

---

Thank you for checking out the **8-Puzzle Problem Solver**! Contributions, suggestions, and feedback are always welcome.
