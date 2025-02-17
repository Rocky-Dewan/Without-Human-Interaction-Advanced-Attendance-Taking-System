import firebase_admin
import firebase_config

from firebase_admin import credentials, db

# Initialize Firebase


# Reference to the database
students_ref = db.reference('students')
attendance_ref = db.reference("attendance")
