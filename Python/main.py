from cv2 import *
from functions import *
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import os
import sys
from tqdm import tqdm
from time import sleep

n = len(sys.argv)
image_name = sys.argv[1]

#for i in tqdm(range(100), desc="Generating Matte", ascii=False, ncols=75):
main(image_name)
    #sleep(0.01)
    

#print("Done!")
