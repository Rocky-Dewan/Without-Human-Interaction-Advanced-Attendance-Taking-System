from classroom.firebase_config import ref

def mark_attendance(student_id):
    ref.child(student_id).update({'attendance': 'present'})

def get_student_details(student_id):
    return ref.child(student_id).get()
