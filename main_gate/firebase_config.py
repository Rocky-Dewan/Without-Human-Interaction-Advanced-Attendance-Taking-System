import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
#collect from me ....

# Reference to the database
students_ref = db.reference('students')
attendance_ref = db.reference("attendance")
