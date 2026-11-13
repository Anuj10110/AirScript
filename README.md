# AirScript ✍️

**Vision-Based Air-Writing Recognition and Intelligent Digital Notepad**

AirScript is a Python-based computer vision project that allows users to write in the air using hand gestures. It tracks the user's index fingertip through a webcam and renders movements on a persistent digital canvas.

AirScript also integrates a Convolutional Neural Network (CNN) trained on the MNIST dataset to recognize handwritten digits from the drawing canvas.

## Current Features

- Real-time webcam feed.
- Hand tracking using MediaPipe.
- Index fingertip position detection.
- Gesture-based drawing using the index finger.
- Persistent digital drawing canvas.
- Clear the canvas using keyboard controls.
- Live gesture status displayed on the camera feed.
- CNN-based handwritten digit recognition (0–9).
- Real-time digit prediction with confidence scores.
- MNIST-based model training using PyTorch.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe | Hand tracking and landmark detection |
| NumPy | Numerical operations and image processing |
| PyTorch | CNN model development and training |
| Torchvision | MNIST dataset and image transformations |

## Project Structure

```text
AirScript/
├── data/                       # MNIST dataset (ignored by Git)
├── models/                     # Model files (ignored by Git)
│   ├── hand_landmarker.task
│   └── digit_cnn.pth
├── src/
│   ├── airscript/
│   │   ├── __init__.py
│   │   ├── camera.py
│   │   ├── hand_tracker.py
│   │   ├── stroke.py
│   │   ├── drawing_canvas.py
│   │   ├── digit_model.py
│   │   ├── digit_predictor.py
│   │   └── train_model.py
│   └── main.py
├── tests/
│   └── test_digit.py
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
python -m pip install --upgrade pip
pip install opencv-python mediapipe numpy torch torchvision
```

### 4. Download the MediaPipe hand landmark model

Create the models directory:

```bash
mkdir -p models
```

Download the official MediaPipe Hand Landmarker model and save it as:

```text
models/hand_landmarker.task
```

Official documentation:  
https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker

### 5. Train the digit recognition model

AirScript uses a CNN trained on the MNIST handwritten digit dataset.

Run:

```bash
PYTHONPATH=src python src/airscript/train_model.py
```

The training script automatically downloads MNIST, trains the CNN, evaluates its accuracy, and saves the trained model to:

```text
models/digit_cnn.pth
```

**Note:** Model files and datasets are excluded from Git. You must download the hand landmark model and train the digit recognition model locally before running AirScript.

## Run AirScript

From the project root, with the virtual environment activated:

```bash
PYTHONPATH=src python src/main.py
```

Make sure both required model files are available in the `models/` directory.

## Controls

| Control / Gesture | Action |
|---|---|
| Raise your index finger | Draw on the canvas |
| Make a fist or lower other fingers | Stop drawing |
| `P` | Predict the handwritten digit |
| `C` | Clear the canvas |
| `Q` | Quit the application |

## Digit Recognition Model

AirScript uses a Convolutional Neural Network (CNN) built with PyTorch.

The model:
- Uses convolutional and max-pooling layers for feature extraction.
- Uses fully connected layers for digit classification.
- Recognizes handwritten digits from 0 to 9.
- Is trained using the MNIST dataset.
- Preprocesses canvas drawings into 28 × 28 images before prediction.

**Training Performance**

- Dataset: MNIST
- Training epochs: 5
- Optimizer: Adam
- Loss function: Cross Entropy Loss
- Test accuracy: 99.09%

*Accuracy represents performance on the MNIST test dataset; real-world air-written recognition may vary.*

## Roadmap

- [ ] Improve prediction accuracy for air-written digits.
- [ ] Collect a custom dataset of air-written digits.
- [ ] Improve fingertip movement smoothing.
- [ ] Improve gesture detection reliability.
- [ ] Combine the camera feed and drawing canvas into one interface.
- [ ] Extend recognition beyond digits to alphabets and words.
- [ ] Develop intelligent digital-notepad features.

## Project Status

AirScript is under active development.

Currently implemented:
- Real-time webcam access.
- MediaPipe-based hand tracking.
- Gesture-controlled air-writing.
- Persistent digital drawing canvas.
- CNN-based handwritten digit recognition.

The next development phase focuses on improving recognition accuracy using real-world air-written samples and expanding the system's capabilities.

---

**Developed by Anuj Taneja**