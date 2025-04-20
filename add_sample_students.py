import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("iot-attendance-system-914b1-firebase-adminsdk-fbsvc-7af87f1206.json")  # Use your downloaded key
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-attendance-system-914b1-default-rtdb.firebaseio.com/"  # Change this to your Firebase URL
})

# Sample Student Data
students_data = {
    "1001": {
        "name": "Rocky",
        "barcode": "1234",
        "image_url": "rocky.jpg"
    },
    "1002": {
        "name": "Dewan",
        "barcode": "4321",
        "image_url": "dewan.jpg"
    }
}

# Upload Data to Firebase
ref = db.reference("students")
ref.set(students_data)

print("Sample students added successfully!")
