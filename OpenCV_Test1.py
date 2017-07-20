import os
import cv2

#path = "d:/_temp/"
path = ""
filename = "sample1.jpg"
cascade_filename = "haarcascade_frontalface_alt.xml"

#Read images from File
tmpname1 = path + filename;
img = cv2.imread(tmpname1)
cv2.imshow('Original', img)
cv2.waitKey(0)

#Glay Scale
img_glayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Glay Scale', img_glayscale)
tmpname2 = path +  "GlayScaled_" + filename;
# cv2.imwrite(tmpname2, img_gs)
cv2.waitKey(0)

#Binary
ret, img_binary = cv2.threshold(img_glayscale, 100, 250,  cv2.THRESH_BINARY)
cv2.imshow('Binary', img_binary)
tmpname3 = path + "Binary_" + filename;
# cv2.imwrite(tmpname3, img)
cv2.waitKey(0)

#Resize
img_resize = cv2.resize(img, dsize =(1280, 720))
cv2.imshow('Resize', img_resize)
tmpname4 = path + "Resize_" + filename;
# cv2.imwrite(tmpname4, img)
cv2.waitKey(0)

#Detect Face
cascade_file = path + cascade_filename
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(img_glayscale, minSize=(150, 150))
if len(face_list) == 0:
    print("Fail! can't detect face.")
    quit()
# Draw red rectangle as face area
for (x, y, w, h) in face_list:
    print("coordinate= ", x, y, w, h)
    color = (0, 0, 255)
    pen_w = 8
    cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness=pen_w)
cv2.imshow('Detect Face', img)
tmpname5 = path + "DetectFace_" + filename;
# cv2.imwrite(tmpname5, img)
cv2.waitKey(0)

cv2.destroyAllWindows()
