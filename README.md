This is a Python wrapper of the imagemorph repository by Lambert Schomaker
(see last section). Rather than using the `imagemorph` executable and writing the
result to disk, the `imagemorph.py` module provides a Python wrapper function
which takes as input an image and returns a morphed image, which is
equivalent to applying the `imagemorph` executable.

Any image type can be processed (not just .ppm), as long as it can be
loaded with OpenCV.

The code was tested on Linux, using Python 3.6.

### Required packages

Running the Python script requires `numpy` and `opencv`, which can be installed
with pip:

```
pip install numpy opencv-python
```

### How to run

First create a dynamic library from the C code: 

```
make imagemorph.so
```

This creates a shared library that is required for running the `imagemorph.py`
module. For a demo of the module, run

```
python imagemorph.py
```

which will apply the elastic morphing to the `sampled-input.png` image and save
the result to `out.png`.


# imagemorph.c
Program to apply random elastic rubbersheet  transforms to Netpbm color (.ppm) images for  augmenting training sets in machine learning/deep learning.  The program reads an input .ppm image from stdin and writes a ppm image to stdout.  Original Author: Marius Bulacu (.pgm version for characters). Adapted for .ppm and color: Lambert Schomaker

Please cite:

M Bulacu, A Brink, T van der Zant, L Schomaker (2009).
Recognition of handwritten numerical fields in a 
large single-writer historical collection,
10th International Conference on Document Analysis and Recognition, 
pp. 808-812, DOI: 10.1109/ICDAR.2009.8 
