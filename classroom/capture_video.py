import cv2
import time

def capture_video():
    """Records 2 minutes of video from the classroom camera."""
    cap = cv2.VideoCapture(0)  # Use default webcam
    if not cap.isOpened():
        print("❌ Error: Camera not accessible!")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('classroom_recording.avi', fourcc, 10.0, (640, 480))

    print("🎥 Recording started...")
    start_time = time.time()

    while time.time() - start_time < 120:  # Record for 2 minutes
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow("Classroom Feed", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to stop manually
            break

    print("✅ Recording complete. Processing video for face recognition...")

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video()
