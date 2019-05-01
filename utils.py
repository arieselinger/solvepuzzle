import matplotlib.pyplot as plt
import numpy as np
import problem
from config import *
from PIL import Image
import os

def cut_image(img, verbose=False):
    # Create an array to shuffle blocks
    new_img = np.zeros((N_ROW, N_COL, HEIGHT_BLOCK, WIDTH_BLOCK))
    if verbose: print(new_img.shape)
    for row in range(N_ROW):
        for col in range(N_COL):
            new_img[row, col] = img[row*HEIGHT_BLOCK:(row+1)*HEIGHT_BLOCK, col*WIDTH_BLOCK:(col+1)*WIDTH_BLOCK]
    return new_img

def recreate_cut_image(cut_img):
    # Recreate an image 
    recreated_img = np.zeros(((HEIGHT, WIDTH)))
    for row in range(N_ROW):
        for col in range(N_COL):
            recreated_img[row*HEIGHT_BLOCK:(row+1)*HEIGHT_BLOCK, col*WIDTH_BLOCK:(col+1)*WIDTH_BLOCK] = cut_img[row, col]
    return recreated_img

def print_all_blocks(cut_img):
    for row in range(N_ROW):
        for col in range(N_COL):
            plt.imshow(cut_img[row, col])
            plt.show()

def evaluate(cut_img):
    value = 0
    for row in range(1,N_ROW-1):
        for col in range(1,N_COL-1):
            # TOP
            layer1 = cut_img[row,col,0]
            layer2 = cut_img[row-1,col,HEIGHT_BLOCK-1]
            value += np.mean(np.absolute(layer1-layer2))

            # DOWN
            layer1 = cut_img[row,col,HEIGHT_BLOCK-1]
            layer2 = cut_img[row+1,col,0]
            value += np.mean(np.absolute(layer1-layer2))

            # LEFT
            layer1 = cut_img[row,col,:,0]
            layer2 = cut_img[row,col-1,:,HEIGHT_BLOCK-1]
            value += np.mean(np.absolute(layer1-layer2))

            # RIGHT
            layer1 = cut_img[row,col,:,HEIGHT_BLOCK-1]
            layer2 = cut_img[row,col+1,:,0]
            value += np.mean(np.absolute(layer1-layer2))

    return value

def evaluate2(cut_img):
    value = 0

    for row in range(N_ROW-1):
        for col in range(N_COL):
            # DOWN
            layer1 = cut_img[row,col,HEIGHT_BLOCK-1]
            layer2 = cut_img[row+1,col,0]
            value += np.mean(np.absolute(layer1-layer2))

    for col in range(N_COL-1):
        for rol in range(N_ROW):
            # RIGHT
            layer1 = cut_img[row,col,:,HEIGHT_BLOCK-1]
            layer2 = cut_img[row,col+1,:,0]
            value += np.mean(np.absolute(layer1-layer2))

    return value

