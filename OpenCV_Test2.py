import os
import cv2

#path = "d:/_temp/"
path = ""
filename = "sample2.jpg"
cascade_filename = "cascade.xml"

#Read images from File
tmpname1 = path + filename;
img = cv2.imread(tmpname1)
#Glay Scale
img_glayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect Symbol
cascade_file = path + cascade_filename
cascade = cv2.CascadeClassifier(cascade_file)
symbol_list = cascade.detectMultiScale(img_glayscale, minSize=(150, 150))
if len(symbol_list) == 0:
    print("Fail! can't detect symbol.")
    quit()
# Draw red rectangle as symbol area
for (x, y, w, h) in symbol_list:
    print("coordinate= ", x, y, w, h)
    color = (0, 0, 255)
    pen_w = 8
    cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness=pen_w)
cv2.imshow('Detect Symbol', img)
tmpname5 = path + "DetectSymbol_" + filename;
# cv2.imwrite(tmpname1, img)
cv2.waitKey(0)

cv2.destroyAllWindows()
