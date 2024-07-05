import os
import cv2
import matplotlib.pyplot as plt
import adaboost
def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    """
    Begin this part by reading the datapath given which contains a detectData.txt
      Start to divide between each lines and each spaces
      If that line consists of less than or equal to two things,
      take the first thing which is the image's file name and 
      use the cv2.imread to extract the numpy.ndarray of the image
      Else which means the line consists of the coordinates of the faces' coordinates
      save the coordinates and add the width and height to the left top coordinate
    Crop each of the faces' images by slicing and 
    Resize to the wanted size (19*19) using cv2.resize
    Convert colorspace from bgr to grayscale using cv2.cvtColor method
    Classify the results and if it is classified as face (=1)
    use cv2.rectangle and draw a green box, else draw a red box
    Last, we show the whole images using cv2.imshow including the rectangles we added

    Results:
    After trained by training datasets and tested by testing datasets
    In this part, we are required to do it on images 
    and detect if the faces are detected as a face or not
    For the pictures given to us, the number of faces detected decreased as the T increases
    the same goes for part 5, which is using the pictures we chose ourselves
    This might happened because as the T increases,
    the learned features are getting more specific (overfitting),
    which causes some faces not detected in the end
    
    """
    newlines=[]
    f = open(dataPath, "r")
    lines = f.readlines()
    imgs = []
    list_of_boxes = []
    wk = {}
    
    for i in lines:
      newlines.append(i.split('\n')[0])
    # print(newlines)
    head = ""
    wk["pic_name"] = []
    for i in newlines:
      x = i.split(' ')
      # print(x)
      if(len(x)<=2):
        head = x[0]         # x[0] contains files' names
        wk[head] = []
        wk["pic_name"].append(x[0])
        wk["numpyarray"+x[0]] = cv2.imread('data/detect/' + x[0])
      else:
        box = [None] * 4
        for j in range (4):
          box[j] = x[j]
          # print(box[j])
        wk[head].append(box)
    # print(wk[head])
    # print(wk[wk["pic_name"][x]])

    numparr = []
    numofimgs = len(wk["pic_name"])
    for x in range (numofimgs):
      # print("File's name: ", wk["pic_name"][x])
      # print("Coordinates: ")
      # for i in wk[wk["pic_name"][x]]:
        # print(i)
      # print("Image's numpy array: ")
      # print(wk["numpyarray"+wk["pic_name"][x]])
      numparr.append(wk["numpyarray"+wk["pic_name"][x]])
      # print(numparr[x])

    faces = []
    for i in range (numofimgs):
      for j in wk[wk["pic_name"][i]]:
        x1 = 0
        y1 = 0 
        x2 = 0
        y2 = 0
        x1 = int(j[0])              # coordinates of left top in x
        y1 = int(j[1])              # coordinates of left top in y
        x2 = int(j[0]) + int(j[2])  # the width added to produce the right bottom x
        y2 = int(j[1]) + int(j[3])  # the height added to produce the right bottom y
        #crop -> resize -> change to grayscale -> give cls.classify()
        crop = numparr[i][y1:y2, x1:x2]         # [y:y+h,x:x+w] and crop is nparray type
        resized = cv2.resize(crop, (19, 19), interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)        # change from BGR to grayscale
        # print(type(gray))
        faces.append(gray)
    
    for i in range (numofimgs):
      for j,face in zip(wk[wk["pic_name"][i]],faces):
        if(clf.classify(face)):                 # the face images(hasil potongan) are classified by clf.classify
          ni = cv2.rectangle(numparr[i], (int(j[0]), int(j[1])), (int(j[0])+int(j[2]), int(j[1])+int(j[3])), (0,255,0), 2)
        else:
          ni = cv2.rectangle(numparr[i], (int(j[0]), int(j[1])), (int(j[0])+int(j[2]), int(j[1])+int(j[3])), (0,0,255), 2)
      
      gray2 = cv2.cvtColor(numparr[i], cv2.COLOR_BGR2RGB)
      fig, ax = plt.subplots(1, 1)
      ax.axis('off')
      ax.imshow(gray2)
      plt.show()

      cv2.waitKey(0)
      cv2.destroyAllWindows()

    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)

clf = adaboost.Adaboost.load('clf_200_1_10')
# detect('data/detect/detectData.txt', clf)
detect('data/detect/myImages.txt', clf)