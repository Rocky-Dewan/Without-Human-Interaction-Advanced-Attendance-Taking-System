import time
import firebase_config  # Import Firebase setup
from firebase_admin import db
from datetime import datetime

def scan_barcode():
    """Simulate barcode scanning with user input"""
    barcode = input("🔹 Scan barcode (Enter student barcode manually): ")

    # Fetch student data from Firebase
    students_ref = db.reference("students")
    student_data = students_ref.get()

    # Check if barcode exists in database
    student_found = None
    for student_id, data in student_data.items():
        if data["barcode"] == barcode:
            student_found = {"id": student_id, "name": data["name"]}
            break

    if student_found:
        print(f"✅ Student Found: {student_found['name']} (ID: {student_found['id']})")
        
        # Mark entry time
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance_ref = db.reference(f"attendance/{student_found['id']}")
        attendance_ref.set({
            "name": student_found["name"],
            "barcode": barcode,
            "entry_time": entry_time,
            "verified": False  # This will be updated after face recognition
        })
        
        print(f"✅ Entry recorded at {entry_time}")
    else:
        print("❌ Invalid Barcode! Student not found.")

if __name__ == "__main__":
    while True:
        scan_barcode()
        time.sleep(2)  # Wait before next scan (simulate real-life scanning)
