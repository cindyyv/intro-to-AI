import os
import cv2

def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1) 
    """
    In this part1, we need to load and prepare our dataset
    First thing first, direct the datapath to 
    images' folders and files using the os library imported
    read the images using cv2.imread and get the numpy.ndarray of the image
    store the numpy array of images to dataset by appending to list
    
    Results:
    Numpy array of images returned to main.py to load the images

    """
    dataset = []
    sets = os.listdir(dataPath)
    for folders in sets:
      # print(folders)
      if folders == 'non-face':
        nffile = os.path.join(dataPath, 'non-face')
        nonface = os.listdir(nffile)
        for i in nonface:                                   # i as the pgm filename
          nfdata = cv2.imread(os.path.join(nffile, i), 0)   # data as ndarray file type
          dataset.append((nfdata, 0)) 
      elif folders == 'face':
        ffile = os.path.join(dataPath, 'face')
        face = os.listdir(ffile)
        for i in face:
          fdata = cv2.imread(os.path.join(ffile, i), 0)     #fdata -> numpy aray of m,n representing the image
          dataset.append((fdata, 1)) # no .shape as results is numpyarray with m n dimension (diganti)

    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)
    return dataset