import face_recognition
import cv2

# katherine encoding
katherine = face_recognition.load_image_file('./img/k.jpg')
katherine_encoding = face_recognition.face_encodings(picture_of_me)[0]

# new img from command line
request = sys.argv[0]
img = face_recognition.load_image_file('./img'+request)

# encode all new faces
new_faces = [face_recognition.face_encodings(face)[0]
             for face in face_recognition.face_locations(img)]

# check all new faces against Katherine
results = [face_recognition.compare_faces([katherine_encoding], new_face)
           for new_face in new_faces]

if sum(results) == 0:
    print("No Katherines found :(")
    quit()

# identify katherine in set of faces
new_katherine_index = results.index(True)
# katherine's face
new_katherine = new_faces[new_katherine_index]

# retrieve crown
crown = cv2.imread('./img/crown.png')
crown = cv2.resize(crown, (100, 50))
ktop = new_katherine[:-2]

# retrieve original img in cv form
img = cv2.imread('./img'+request)
# crown dims
crown_height, crown_width = crown.shape[:-1]
# overlay handling alpha channel
for c in range(0,3):
    img[ktop[1]:crown_height, ktop[0]-ktop[2]:crown_width, c] =
    crown[:,:,c] * (crown[:,:,3]/255.0) +  img[ktop[1]:ktop[1]+crown.shape[0], ktop[0]-ktop[2]:ktop[0]-ktop[2]+crown.shape[1], c] * (1.0 - crown[:,:,3]/255.0)

# show
cv2.imshow(img)
