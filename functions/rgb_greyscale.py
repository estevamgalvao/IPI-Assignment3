import numpy as np
import cv2

def RGB2Greyscale(img):
    height, width, channels = img.shape
    # print(channels)
    imageGreyscale = np.zeros((height, width), dtype = np.uint8)

    imageGreyscale[:, :] = (0.114 * img[:, :, 0]) + (0.587 * img[:, :, 1]) + (0.299 * img[:, :, 2])
    return imageGreyscale