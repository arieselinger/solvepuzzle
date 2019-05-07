from config import DATA_FOLDER
from puzzle import Puzzle
import os

# For each image in the data folder
datafiles = os.listdir(DATA_FOLDER)

for filename in datafiles:

    # Create an instance of the puzzle
    filepath = os.path.abspath(os.path.join(DATA_FOLDER, filename))
    problem = Puzzle(filepath)
    
    # Print the puzzle
    problem.print()

    # Shuffle the puzzle
    problem.shuffle()

    # Switch the blocks (0,0) and (8,8)
    problem.move(0,0,8,8)

    # Save the puzzle
    problem.save("example.jpg")
