import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
#collect from me ..

# Sample Student Data
students_data = {
    "1001": {
        "name": "John Doe",
        "barcode": "123456789",
        "image_url": "https://example.com/john.jpg"
    },
    "1002": {
        "name": "Alice Smith",
        "barcode": "987654321",
        "image_url": "https://example.com/alice.jpg"
    }
}

# Upload Data to Firebase
ref = db.reference("students")
ref.set(students_data)

print("Sample students added successfully!")
