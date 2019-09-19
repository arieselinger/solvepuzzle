from config import DATASETS
from puzzle import Puzzle
from time import time
import jsonlines
import os

# For each image in the data folder
ROW_FOLDER = os.path.join(DATASETS, "row")
datafiles = os.listdir(ROW_FOLDER)

for filename in datafiles:

    filepath = os.path.abspath(os.path.join(ROW_FOLDER, filename))
    print(filepath)

    # Create an instance of the puzzle
    problem = Puzzle(filepath)
    
    # Print the puzzle
    #problem.print()

    # Generate images with k block transpositions
    for k in range(1,10):
        
        for _ in range(2):

            # Re-initialize the puzzle
            problem.reinit()

            # Transpose the blocks
            target = problem.permute(k=k)

            # Print the image
            #problem.print()

            # Save the image
            new_filename = str(int(time()*1000))+'_'+str(target)+'_'+filename
            problem.save(pathname=os.path.join(DATASETS, "supervised", new_filename))

            # Save the target
            obj = {'filename' : new_filename, 'target': target}
            with jsonlines.open(os.path.join(DATASETS, 'targets.jsonl'), 'a') as f:
                f.write(obj)

    break
