import cv2
import numpy as np

cap = cv2.VideoCapture("traffic_video.mp4")

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Threshold to remove gray regions
    _, fgmask = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    # Morphological operations
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vehicle_count = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Filter small contours
        if area > 2000:
            vehicle_count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Density classification
    if vehicle_count < 5:
        density = "LOW"
        color = (0, 255, 0)
    elif 5 <= vehicle_count < 15:
        density = "MEDIUM"
        color = (0, 255, 255)
    else:
        density = "HIGH"
        color = (0, 0, 255)

    cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(frame, f"Density: {density}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Traffic Monitoring", frame)
    cv2.imshow("Foreground Mask", fgmask)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
