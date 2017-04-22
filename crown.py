import cv2
import re
import sys

request = sys.argv[1]

# running crown placement separately in OpenCV because can't import cv 3.2.0
# with py 3.6, currently, for some reason

# obtain new_katherine from k.txt

# regexp pattern
pattern = re.compile('[\W_]+')
# clean it up!
with open('k.txt', 'r') as f:
    new_katherine = tuple([int(val) for val in
                            [pattern.sub('', substr) for substr in
                                f.readline()[1:-1].split(',')]
                          ])

print(new_katherine)

# retrieve crown
crown = cv2.imread('./img/crown.png')
crown = cv2.resize(crown, (100, 50))
ktop = new_katherine[:-2]

# retrieve original img in cv form
img = cv2.imread('./img/'+request)
# crown dims
crown_height, crown_width = crown.shape[:-1]
# overlay handling alpha channel
for c in range(0,3):
    img[ktop[1]:crown_height, (ktop[0]-ktop[2]):crown_width, c] = crown[:,:,c] * (crown[:,:,3]/255.0) +  img[ktop[1]:ktop[1]+crown.shape[0], (ktop[0]-ktop[2]):ktop[0]-ktop[2]+crown.shape[1], c] * (1.0 - crown[:,:,3]/255.0)

# show
cv2.imshow(img)
