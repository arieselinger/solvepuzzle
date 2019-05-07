import os
import numpy as np
import utils
import matplotlib.pyplot as plt
import matplotlib.image as image
from PIL import Image

from config import SAVE_FOLDER, HEIGHT, WIDTH, N_ROW, N_COL, HEIGHT_BLOCK, WIDTH_BLOCK

class Puzzle:
    ''' 
    A class that defines a puzzle.
    
    It defines two kinds of images:

    1. self.original_img : np.array of shape (HEIGHT, WIDTH)
    2. self.cut_img : np.array of shape (N_ROW, N_COL, HEIGHT_BLOCK, WIDTH_BLOCK)

    Therefore, self.cut_img[i][j] represents the sub-image at the row i and the col j
    '''

    def __init__(self, filepath):

        # Open image
        self.img_path = filepath
        self.original_img = Image.open(self.img_path).convert("L")

        # Resize image
        self.original_img = self.original_img.resize((WIDTH, HEIGHT))
        self.original_img = np.asarray(self.original_img)

        # Create cut_image with shape (N_ROW, N_COL, HEIGHT_BLOCK, WIDTH_BLOCK)
        self.cut_img = utils.cut_image(self.original_img)
    
    def print(self):
        '''
        Shows the whole puzzle
        '''
        img = utils.recreate_cut_image(self.cut_img)
        plt.imshow(img, cmap='gray')
        plt.show()
    
    def print_block(self,i,j):
        '''
        Show the block found at row i and col j with :

        0 <= i <= N_ROW -1

        0 <= j <= N_COL -1
        '''
        assert (i in range(N_ROW) and j in range(N_COL))
        plt.imshow(self.cut_img[i][j], cmap='gray')
        plt.show()

    def shuffle(self):
        np.random.shuffle(self.cut_img.reshape(N_ROW*N_COL, HEIGHT_BLOCK, WIDTH_BLOCK))
        self.cut_img.reshape(N_ROW, N_COL, HEIGHT_BLOCK, WIDTH_BLOCK)

    def move(self, i1, j1, i2,j2):
        block1 = self.cut_img[i1][j1].copy()
        block2 = self.cut_img[i2][j2].copy()
        self.cut_img[i1,j1], self.cut_img[i2,j2] = block2, block1
    
    def save(self, filename):
        filepath = os.path.join(SAVE_FOLDER, filename)
        if not os.path.exists(filepath):
            to_save_img = utils.recreate_cut_image(self.cut_img)
            plt.imsave(filepath, utils.recreate_cut_image(self.cut_img), cmap="gray")

