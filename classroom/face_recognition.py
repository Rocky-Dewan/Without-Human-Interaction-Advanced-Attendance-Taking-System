import cv2
import face_recognition
import firebase_config
from firebase_admin import db
import numpy as np
import os

def load_known_faces():
    """Loads known student images and encodes them."""
    students_ref = db.reference("students")
    students_data = students_ref.get()

    known_face_encodings = []
    known_face_names = []

    for student_id, student in students_data.items():
        img_url = student["image_url"]
        img_path = f"students/{student_id}.jpg"  # Assume images are stored locally

        # Load and encode student face
        if os.path.exists(img_path):
            image = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(student_id)

    return known_face_encodings, known_face_names

def recognize_faces(video_path="classroom_recording.avi"):
    """Detects students in the recorded video and updates attendance."""
    known_face_encodings, known_face_names = load_known_faces()
    cap = cv2.VideoCapture(video_path)

    present_students = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for face recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            if True in matches:
                match_index = matches.index(True)
                student_id = known_face_names[match_index]
                present_students.add(student_id)

    cap.release()
    cv2.destroyAllWindows()

    # Update attendance in Firebase
    attendance_ref = db.reference("attendance")
    for student_id in present_students:
        attendance_ref.child(student_id).update({"verified": True})

    print(f"✅ Attendance updated for {len(present_students)} students.")

if __name__ == "__main__":
    recognize_faces()
