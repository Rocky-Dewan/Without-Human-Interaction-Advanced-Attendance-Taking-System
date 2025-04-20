import firebase_admin
import firebase_config

from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("iot-attendance-system-914b1-firebase-adminsdk-fbsvc-c832ed67dc.json")  # Use your downloaded key
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-attendance-system-914b1-default-rtdb.firebaseio.com/"  # Change this to your Firebase URL
})

# Reference to the database
students_ref = db.reference('students')
attendance_ref = db.reference("attendance")
