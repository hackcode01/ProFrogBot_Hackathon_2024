import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("./photos/photo.jpg")
template = cv2.imread("image_1.png")

face_width = 190
face_height = 240

x_offset = 167
y_offset = 180
roi = template[y_offset:y_offset+face_height, x_offset:x_offset+face_width]

height, width = image.shape[:2]
max_height = 800
max_width = 1200

if height > max_height or width > max_width:
    scale = min(max_height / height, max_width / width)
    new_height = int(height * scale)
    new_width = int(width * scale)
    image = cv2.resize(image, (new_width, new_height))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.3,
                                      minNeighbors=5,
                                      minSize=(30, 30))

for (x, y, w, h) in faces:
    face_roi = image[y:y+h, x:x+w]
    face_resized = cv2.resize(face_roi, (face_width, face_height))

    result = cv2.addWeighted(roi, 0.1, face_resized, 0.9, 0)

    template[y_offset:y_offset+face_height, x_offset:x_offset+face_width] = result

    cv2.imwrite(f"result_1.jpg", template)

    break
