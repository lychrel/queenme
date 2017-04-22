import cv2
import re
import sys
import numpy as np
from random import choice

# font
font = cv2.FONT_HERSHEY_PLAIN

request = sys.argv[1]

# running crown placement separately in OpenCV because can't import cv 3.2.0
# with py 3.6, currently, for some reason

# obtain new_katherine from k.txt

# pattern: only keep alphanumeric
pattern = re.compile('[\W_]+')
# clean up data string
with open('k.txt', 'r') as f:
    new_katherine = tuple([int(val) for val in
                            [pattern.sub('', substr) for substr in
                                f.readline()[1:-1].split(',')]])
# top, right, bottom, left
print(new_katherine)

# retrieve crown
crown = cv2.imread('./img/crown.png')
crown = cv2.resize(crown, (100, 50))

ktop = new_katherine[0]
kleft = new_katherine[3]

# retrieve original img in cv form
img = cv2.imread('./img/'+request)
# crown dims
crown_height, crown_width = crown.shape[:-1]

# place crown
img[(ktop - crown_height):ktop , kleft:kleft+crown_width] = crown

# add random motivational text
phrases = ['werk', 'slay', 'hbd', 'woo']

# image dimensions
width, height = img.shape[:-1]

# sprinkle motivation
for phrase in phrases:
    cv2.putText(img, phrase, (choice(range(width - 60)),choice(range(height - 60))),
                font, 5,(0,255,255),8,cv2.LINE_AA)

# pick coordinates


# show
cv2.imwrite('kqueen.png',img)
