from cv2 import cv2
import numpy

img = cv2.imread("compu_vision/original.png",0)
print(img)


ai = cv2.imwrite("compu_vision/newsmallgray.png", img) #create a new file image

print("/n")

#indexing, slicing and iterating numpy arrays
print(img[0:2, 2:4])

for i in img.T: #iterates all values in the array (.T gives the transppose)
    print(i)

for i in img.flat: #iterates all values one by one
    print(i)





#stacking and splitting numpy arrays
ims=numpy.hstack((img,img)) #horizontally stacking two arrays
print(ims)


ima =numpy.vstack((img,img)) #vertically stacks two arrays together
print(ima)


lst = numpy.hsplit(ims, 5) #splits the giant numpy array into 5 different numpy array
print(lst)
print(lst[0])
