import cv2
import os
import time
import psutil
import requests
from datetime import datetime
from plyer import notification

# =========================
# CONFIG
# =========================

TELEGRAM_BOT_TOKEN = "PUT_YOUR_TOKEN"
TELEGRAM_CHAT_ID = "PUT_YOUR_CHAT_ID"

SD_CARD_PATH = "D:/"   # <-- CHANGE THIS TO YOUR SD CARD LETTER
LOW_SPACE_GB = 1.0

SEGMENT_LENGTH = 10

cap = cv2.VideoCapture(0)

os.makedirs("clips", exist_ok=True)

fps = 20
w = int(cap.get(3))
h = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*"XVID")

# =========================
# ALERT SYSTEM
# =========================

def alert(msg):
    print(msg)

    # laptop popup
    notification.notify(
        title="SD Dashcam Alert",
        message=msg,
        timeout=5
    )

    # phone (Telegram)
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_CHAT_ID, "text": msg},
            timeout=3
        )
    except:
        pass

# =========================
# STORAGE CHECK (SD CARD)
# =========================

def check_sd():
    usage = psutil.disk_usage(SD_CARD_PATH)
    free_gb = usage.free / (1024**3)
    return free_gb

# =========================
# MOTION DETECTION
# =========================

def motion(prev, curr):
    diff = cv2.absdiff(prev, curr)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    return cv2.countNonZero(thresh) > 2000

# =========================
# INIT
# =========================

ret, prev = cap.read()

def new_file():
    return os.path.join(
        SD_CARD_PATH,
        f"clip_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
    )

out_file = new_file()
out = cv2.VideoWriter(out_file, fourcc, fps, (w, h))

start = time.time()
motion_detected = False
alert_sent = False

# =========================
# LOOP
# =========================

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

    if motion(prev, frame):
        motion_detected = True

    prev = frame

    cv2.imshow("SD Dashcam", frame)

    # =========================
    # SD CARD FULL CHECK
    # =========================

    free = check_sd()

    if free < LOW_SPACE_GB and not alert_sent:
        alert(f"⚠️ SD Card almost full: {free:.2f} GB left")
        alert_sent = True

    # =========================
    # SEGMENT ROTATION
    # =========================

    if time.time() - start > SEGMENT_LENGTH:

        out.release()

        if not motion_detected:
            try:
                os.remove(out_file)
            except:
                pass
        else:
            print("Saved:", out_file)

        motion_detected = False
        start = time.time()

        out_file = new_file()
        out = cv2.VideoWriter(out_file, fourcc, fps, (w, h))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
