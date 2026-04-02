"""
Project Name: Object Detection for Rescue Operations
Author: Arindam Gogoi and Krishiv Patel
Model Used: YOLOv8n (yolov8n.pt)

Description:
AI-based drone telemetry system that detects objects,
filters low-confidence detections, and applies a
Target Lock mechanism using center-screen logic.
"""

# =========================cls
# IMPORTS
# =========================
import cv2
import numpy as np
import time
from ultralytics import YOLO


# =========================
# INITIALIZATION
# =========================

# Load YOLOv8 Nano model (Fast and lightweight)
model = YOLO("yolov8n.pt")

# Confidence threshold (remove weak detections)
CONF_THRESHOLD = 0.6


def process_drone_feed(source=0):

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame for better FPS
        frame = cv2.resize(frame, (640, 640))
        height, width, _ = frame.shape

        # =========================
        # YOLO INFERENCE
        # =========================
        results = model(frame)

        for result in results:

            # Vectorized extraction using NumPy
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy()

            for box, conf, cls_id in zip(boxes, confidences, class_ids):

                # =========================
                # CONFIDENCE FILTERING
                # =========================
                # Confidence removes weak detections
                if conf < CONF_THRESHOLD:
                    continue

                x1, y1, x2, y2 = box

                # =========================
                # CENTER POINT CALCULATION
                # =========================
                center_x = (x1 + x2) / 2

                # Define middle 20% of screen
                middle_left = width * 0.4
                middle_right = width * 0.6

                # =========================
                # TARGET LOCK LOGIC
                # =========================
                if middle_left <= center_x <= middle_right:
                    color = (0, 0, 255)  # Red
                    status = "TARGET LOCK"
                else:
                    color = (0, 255, 0)  # Green
                    status = "SCANNING"

                # =========================
                # DISTANCE SIMULATION
                # Smaller box = further away
                # =========================
                box_height = y2 - y1
                distance = round(1000 / (box_height + 1), 2)

                label = f"{model.names[int(cls_id)]} | {conf:.2f}"
                distance_text = f"Dist: {distance} m"

                # =========================
                # DRAWING OVERLAY
                # =========================
                cv2.rectangle(frame,
                              (int(x1), int(y1)),
                              (int(x2), int(y2)),
                              color, 2)

                cv2.putText(frame, label,
                            (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

                cv2.putText(frame, distance_text,
                            (int(x1), int(y2) + 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

                cv2.putText(frame, status,
                            (int(x1), int(y2) + 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, color, 2)

        # =========================
        # FPS COUNTER (Drone HUD)
        # =========================
        current_time = time.time()
        fps = 1 / (current_time - prev_time + 1e-5)
        prev_time = current_time

        cv2.putText(frame, f"FPS: {int(fps)}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 0), 2)

        cv2.imshow("Drone Telemetry System", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # =========================
    # SHUTDOWN
    # =========================
    cap.release()
    cv2.destroyAllWindows()


# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":
    process_drone_feed(0)  # Change to 1 if webcam doesn't open
