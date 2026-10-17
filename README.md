# AirScript ✍️

**Vision-based air-writing recognition and intelligent digital notepad**

AirScript is a Python-based computer vision project that lets users draw in the air using hand gestures. It tracks the index fingertip through a webcam and renders the drawing on a persistent digital canvas.

## Current Features

- Real-time webcam feed.
- Hand tracking using MediaPipe.
- Index fingertip position detection.
- Gesture-based drawing using the index finger.
- Persistent drawing canvas.
- Clear the canvas using the keyboard.
- Live gesture status displayed on the camera feed.

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

## Project Structure

```text
AirScript/
├── models/
│   └── hand_landmarker.task   # Download separately
├── src/
│   ├── airscript/
│   │   ├── camera.py
│   │   ├── hand_tracker.py
│   │   ├── stroke.py
│   │   └── drawing_canvas.py
│   └── main.py
├── tests/
│   ├── test_camera_manual.py
│   ├── test_hand_tracker_manual.py
│   ├── test_stroke_manual.py
│   └── test_drawing_canvas_manual.py
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Anuj10110/AirScript.git
cd AirScript
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install opencv-python mediapipe numpy
```

### 4. Download the hand landmark model

Create the models directory if it doesn't exist:

```bash
mkdir -p models
```

Download the official MediaPipe Hand Landmarker model and save it as:

```text
models/hand_landmarker.task
```

The model file is excluded from Git because it is a downloaded binary. Keep it locally in the `models/` directory.

Official model documentation: https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker

## Run AirScript

From the project root, with the virtual environment activated:

```bash
PYTHONPATH=src python src/main.py
```

## Controls

| Control | Action |
|---|---|
| Raise your index finger | Draw on the canvas |
| Make a fist or lower other fingers | Stop drawing |
| `C` | Clear the canvas |
| `Q` | Quit the application |

## Roadmap

- [ ] Smooth fingertip movement for cleaner strokes.
- [ ] Improve gesture detection reliability.
- [ ] Combine the camera feed and drawing canvas into one window.
- [ ] Explore air-writing character recognition.
- [ ] Develop intelligent digital-notepad features.

## Project Status

AirScript is under active development. Webcam access, hand tracking, gesture-controlled drawing, and the persistent canvas are currently implemented.

