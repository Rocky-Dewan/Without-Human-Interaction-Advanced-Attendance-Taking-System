import face_recognition
import pickle
import os

# Load student images and encode faces
known_face_encodings = []
for image_path in os.listdir("student_images"):
    image = face_recognition.load_image_file(f"student_images/{image_path}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)

# Save embeddings to a file
with open("models/face_embeddings.pickle", "wb") as f:
    pickle.dump(known_face_encodings, f)

print("Face model trained and saved!")
