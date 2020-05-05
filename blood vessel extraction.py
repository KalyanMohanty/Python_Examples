import cv2
import numpy as np
from matplotlib import pyplot as plt

import sklearn
img = cv2.imread('C:/Users/Kalyan Mohanty/Documents/MATLAB/kalyan/good.jpg')
b,g,r = cv2.split(img)

def max_entropy(data):
    # calculate CDF (cumulative density function)
    cdf = data.astype(np.float).cumsum()

    # find histogram's nonzero area
    valid_idx = np.nonzero(data)[0]
    first_bin = valid_idx[0]
    last_bin = valid_idx[-1]

    # initialize search for maximum
    max_ent, threshold = 0, 0

    for it in range(first_bin, last_bin + 1):
        # Background (dark)
        hist_range = data[:it + 1]
        hist_range = hist_range[hist_range != 0] / cdf[it]  # normalize within selected range & remove all 0 elements
        tot_ent = -np.sum(hist_range * np.log(hist_range))  # background entropy

        # Foreground/Object (bright)
        hist_range = data[it + 1:]
        # normalize within selected range & remove all 0 elements
        hist_range = hist_range[hist_range != 0] / (cdf[last_bin] - cdf[it])
        tot_ent -= np.sum(hist_range * np.log(hist_range))  # accumulate object entropy

        # find max
        if tot_ent > max_ent:
            max_ent, threshold = tot_ent, it

    return threshold


img = skimage.io.imread('image.jpg')
# obtain histogram
hist = np.histogram(img, bins=256, range=(0, 256))[0]
# get threshold
th = max_entropy.max_entropy(hist)
print(th)

ret,th1 = cv2.threshold(img,th,255,cv2.THRESH_BINARY)


img0 = cv2.imread('image.jpg',0)
sobelx = cv2.Sobel(img0,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img0,cv2.CV_64F,0,1,ksize=5)  # y
magnitude = np.sqrt(sobelx**2+sobely**2)

img0 = cv2.imread('image.jpg',0)
# # Otsu's thresholding
ret2,th2 = cv2.threshold(img0,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img0,(9,9),5)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

one = Image.fromarray(th2).show()
one = Image.fromarray(th3).show()
