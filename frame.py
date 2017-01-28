#Thanks to Micka from stackoverflow http://stackoverflow.com/users/2393191/micka

#!/usr/bin/env python

import cv2

cap = cv2.VideoCapture(0)

val = False
maxTry = 100 # maximum number of tries to capture a frame from an opened device
cTry = 0

if cap.isOpened(): # if we are able to capture the first frame.
    while (not(val)) and (cTry < maxTry):
        val, frame = cap.read()
        cTry = cTry + 1
else:
    val = False
if val:
    cv2.imwrite('test.png',frame)
else:
    print "No image captured"

cap.release
exit()
