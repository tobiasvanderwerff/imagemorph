from ctypes import *
from pathlib import Path

import cv2 as cv
import numpy as np


class Pixel(Structure):
    """ This class mimics the Pixel structure defined in imagemorph.c. """
    _fields_ = [('r', c_int),
                ('g', c_int),
                ('b', c_int)]


def imagemorph(img, amp, sigma):
    # load C library
    libname = Path.cwd() / 'imagemorph.so'
    c_lib = CDLL(libname)

    # load the imagemorph function from the library
    imagemorph = c_lib.imagemorph
    imagemorph.restype = POINTER(POINTER(Pixel))
    imagemorph.argtypes = [POINTER(POINTER(Pixel)), c_int, c_int, c_double, c_double]

    # convert parameters to C compatible data types
    img_c = (h * POINTER(Pixel))()
    for i in range(h):
        row = (w * Pixel)()
        for j in range(w):
            b, g, r = img[i, j]
            row[j] = Pixel(r, g, b)
        img_c[i] = cast(row, POINTER(Pixel))
    img_c = cast(img_c, POINTER(POINTER(Pixel)))
    amp_c, sigma_c = c_double(amp), c_double(sigma)
    h_c, w_c = c_int(h), c_int(w)
    
    # apply the imagemorph function to the image
    img_c = imagemorph(img_c, h_c, w_c, amp_c, sigma_c)

    res = np.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            px = img_c[i][j]
            res[i, j] = [px.b, px.g, px.r]
    return res


if __name__ == '__main__':
    amp, sigma = 1.3, 3
    img_name = "sample-input.png"
    #img_name = "Zwolle-rgb.ppm"

    # load image
    img = cv.imread(img_name)
    h, w, _ = img.shape

    # apply imagemorph
    res = imagemorph(img, amp, sigma)

    # write result to disk
    cv.imwrite('tmp/out.png', res)
