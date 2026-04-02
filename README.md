# 🚁 Drone Navigator — AI Telemetry & Object Detection System

> Real-time computer vision for autonomous search-and-rescue drone operations, powered by YOLOv8 and OpenCV.

---

## 📌 Overview

**Drone Navigator** is an AI-powered vision system that enables intelligent object detection and tracking for simulated drone rescue operations. It integrates a YOLOv8 deep learning model with a real-time HUD, confidence filtering, and a center-based Target Lock mechanism — mimicking the decision-making of an autonomous rescue drone.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Real-time Detection | YOLOv8-powered inference at ~25–35 FPS |
| 🎯 Target Lock | Locks onto objects in the central 20% of the frame |
| 📊 HUD Display | Live drone heads-up display overlay |
| 📏 Distance Estimation | Simulated depth estimation from bounding box size |
| ✅ Confidence Filtering | Ignores detections below 60% confidence |
| 📦 Multi-object Support | Tracks multiple objects simultaneously |
| ⚡ FPS Monitoring | Real-time performance display |

---

## 🧠 Key Concepts

- **Deep Learning** — YOLOv8 object detection model
- **Computer Vision** — Frame processing and bounding box rendering via OpenCV
- **Confidence Thresholding** — Filters out unreliable detections (≥ 0.6)
- **Intersection over Union (IoU)** — Used in Target Lock logic
- **Real-time Video Pipeline** — Optimized for low-latency inference
- **NumPy** — Efficient center calculation and matrix operations

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLOv8 (Ultralytics) | Object detection model |
| OpenCV | Image processing & visualization |
| NumPy | Mathematical / array operations |

---

## 🔄 System Workflow

```
1. Capture live video feed via OpenCV
2. Resize each frame to 640×640
3. Run YOLOv8 inference
4. Extract bounding boxes & confidence scores
5. Filter detections (confidence ≥ 0.6)
6. Compute object center using NumPy
7. Apply Target Lock logic
8. Render bounding boxes and HUD overlay
9. Display real-time FPS
```

---

## 🎯 Target Lock Logic

The system divides the screen into zones to simulate intelligent drone alignment:

```
┌─────────────────────────────────┐
│                                 │
│    🟢 Scanning Mode             │
│                                 │
│        ┌───────────┐            │
│        │  🔴 Lock  │            │
│        │  Zone     │            │
│        │  (20%)    │            │
│        └───────────┘            │
│                                 │
│    🟢 Scanning Mode             │
│                                 │
└─────────────────────────────────┘
```

- **🔴 Target Locked** — Object center falls within the middle 20% of the frame
- **🟢 Scanning Mode** — Object detected but not yet centered

---

## 📸 Demo

![Detection Screenshot](https://github.com/user-attachments/assets/5e4b4566-52db-4e96-89b9-462adf54a78c)

---

## ⚡ Performance

| Metric | Value |
|---|---|
| Frame Rate | ~25–35 FPS (CPU) |
| Inference Time | ~25–30 ms per frame |
| Input Resolution | 640×640 |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install ultralytics opencv-python numpy
```

### Run

```bash
python drone_detection.py
```

---

## 📁 Project Structure

```
drone-telemetry-system/
│
├── drone_detection.py       # Main detection script
├── screenshots/
│   ├── scanning_mode.png
│   ├── target_lock.png
│   └── fps_display.png
└── README.md
```

---

## 🔮 Roadmap

- [ ] Person-only detection mode for rescue prioritization
- [ ] Crosshair targeting overlay
- [ ] GPS coordinate tagging
- [ ] Edge deployment on Jetson Nano / Raspberry Pi
- [ ] Real drone hardware integration (MAVLink / ROS)
- [ ] Alert system for locked targets

---

## 👤 Author

**Arindam Gogoi**

---

## 📄 License

This project is open source. Feel free to fork, improve, and contribute.
