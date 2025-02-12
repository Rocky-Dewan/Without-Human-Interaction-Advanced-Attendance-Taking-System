import time
import random

def trigger_buzzer():
    """Triggers the buzzer at a random time within a 1-hour class period."""
    class_duration = 60 * 60  # 1 hour in seconds
    random_time = random.randint(10 * 60, 50 * 60)  # Between 10-50 minutes
    print(f"⏳ Buzzer will sound in {random_time // 60} minutes...")

    time.sleep(random_time)
    print("🔔 Buzzer Activated! Capturing video for 2 minutes...")

if __name__ == "__main__":
    trigger_buzzer()
