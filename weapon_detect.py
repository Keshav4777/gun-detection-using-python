import cv2
import imutils
import time
import os

# -----------------------------
# Load Cascade File
# -----------------------------
cascade_path = "gun_cascade.xml"   # make sure this file is in the same folder

if not os.path.exists(cascade_path):
    print("[ERROR] Cascade file not found:", cascade_path)
    exit()

gun_cascade = cv2.CascadeClassifier(cascade_path)

if gun_cascade.empty():
    print("[ERROR] Failed to load cascade file!")
    exit()

# -----------------------------
# Choose input mode
# -----------------------------
print("Select Mode:")
print("1. Webcam")
print("2. Image")
print("3. Video File")
choice = input("Enter choice (1/2/3): ")

# -------------------------------------------------
# 1) Webcam Detection
# -------------------------------------------------
if choice == "1":
    cap = cv2.VideoCapture(0)
    print("[INFO] Starting webcam... Press ESC to exit.")

    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Could not access webcam.")
            break

        frame = imutils.resize(frame, width=800)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        guns = gun_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw bounding boxes
        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Weapon Detected",
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 0, 255), 2)

        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Weapon Detection - Webcam", frame)

        if cv2.waitKey(1) == 27:   # ESC exits
            break

    cap.release()
    cv2.destroyAllWindows()

# -------------------------------------------------
# 2) Image Detection
# -------------------------------------------------
elif choice == "2":
    img_path = input("Enter image path: ")
    img = cv2.imread(img_path)

    if img is None:
        print("[ERROR] Could not load image.")
        exit()

    img = imutils.resize(img, width=800)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in guns:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, "Weapon Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Weapon Detection - Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -------------------------------------------------
# 3) Video File Detection
# -------------------------------------------------
elif choice == "3":
    video_path = input("Enter video path: ")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("[ERROR] Could not load video.")
        exit()

    print("[INFO] Processing video... Press ESC to exit.")

    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=800)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        guns = gun_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Weapon Detected", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Weapon Detection - Video", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    print("[ERROR] Invalid choice!")
