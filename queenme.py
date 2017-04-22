import face_recognition
# grumble grumble
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
# import cv2

# katherine encoding
katherine = face_recognition.load_image_file('./img/k.jpg')
katherine_encoding = face_recognition.face_encodings(katherine)[0]

# new img from command line
request = sys.argv[1]
img = face_recognition.load_image_file('./img/'+request)

# encode all new faces
encoded_faces = face_recognition.face_encodings(img)

# check all new faces against Katherine
results = [face_recognition.compare_faces([katherine_encoding], encoded_face)
           for encoded_face in encoded_faces]

# flatten
results = [item for sublist in results for item in sublist]

if sum(results) == 0:
    print("No Katherines found :(")
    quit()

print("found Katherine!")

# identify katherine's index in set of faces
new_katherine_index = results.index(True)
# pick katherine from those faces
new_katherine = face_recognition.face_locations(img)[new_katherine_index]

# DEBUG
print(new_katherine)

# write out katherine (since cv2 won't import)
target = open('k.txt', 'w')
target.truncate()
target.write(str(new_katherine))
target.close()

# retrieve crown
# crown = cv2.imread('./img/crown.png')
# crown = cv2.resize(crown, (100, 50))
# ktop = new_katherine[:-2]

# retrieve original img in cv form
# img = cv2.imread('./img'+request)
# crown dims
# crown_height, crown_width = crown.shape[:-1]
# overlay handling alpha channel
# for c in range(0,3):
#    img[ktop[1]:crown_height, (ktop[0]-ktop[2]):crown_width, c] =
#    crown[:,:,c] * (crown[:,:,3]/255.0) +  img[ktop[1]:ktop[1]+crown.shape[0], (ktop[0]-ktop[2]):ktop[0]-ktop[2]+crown.shape[1], c] * (1.0 - crown[:,:,3]/255.0)

# show
# cv2.imshow(img)
