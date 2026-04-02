🚁 Drone Navigator’s Telemetry System
🔍 Object Detection for Rescue Operations

An AI-powered real-time drone vision system built using YOLOv8 and OpenCV to simulate intelligent search-and-rescue operations.

📌 Overview

This project demonstrates how Computer Vision and Deep Learning can be integrated into drone systems to enable autonomous detection and tracking of objects in real time.

The system processes live video input, detects objects, filters unreliable detections, and applies a Target Lock mechanism to simulate drone-based rescue targeting.

🚀 Features

✔ Real-time object detection using YOLOv8
✔ Confidence threshold filtering (≥ 0.6)
✔ Intelligent Target Lock system (center-based logic)
✔ Drone Heads-Up Display (HUD)
✔ Simulated distance estimation
✔ FPS (Frames Per Second) monitoring
✔ Multi-object detection support

🧠 Key Concepts Implemented
Deep Learning (YOLOv8)
Computer Vision (OpenCV)
Bounding Box Processing
Confidence Thresholding
Intersection over Union (IOU)
Real-time Video Processing
NumPy-based computations
🛠️ Tech Stack
Technology	Purpose
Python	Core programming
YOLOv8 (Ultralytics)	Object detection
OpenCV	Image processing & visualization
NumPy	Mathematical operations
🎯 System Workflow
Capture live video feed using OpenCV
Resize frame to 640×640
Perform YOLOv8 inference
Extract bounding boxes & confidence scores
Apply confidence filtering
Calculate object center using NumPy
Apply Target Lock logic
Render bounding boxes and HUD
Display FPS
🎯 Target Lock Logic
If object lies in the middle 20% of the screen → 🔴 Target Locked
Otherwise → 🟢 Scanning Mode

This simulates intelligent drone alignment in rescue missions.

📷 Output

👉 Add your screenshots here (drag & drop images after uploading)

Example: <img width="964" height="1012" alt="Screenshot 4" src="https://github.com/user-attachments/assets/5e4b4566-52db-4e96-89b9-462adf54a78c" />

▶️ How to Run
pip install ultralytics opencv-python numpy
python drone_detection.py
📈 Performance
⚡ ~25–35 FPS (CPU-based inference)
⏱️ ~25–30 ms per frame
🎯 Real-time detection capability
📁 Project Structure
drone-telemetry-system/
│
├── drone_detection.py
├── screenshots/
│   ├── scanning_mode.png
│   ├── target_lock.png
│   └── fps_display.png
├── README.md
🔮 Future Improvements
Person-only detection for rescue missions
Crosshair targeting system 🎯
GPS tagging integration
Deployment on Jetson Nano / Raspberry Pi
Real drone hardware integration
📌 Author

Arindam Gogoi
