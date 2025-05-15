# Acne Classification System
<div align="center">
  <img src="https://github.com/rahulkumargit1/acne-classification-system/blob/main/python.jpg" alt="Rahul Kumar's GitHub Cover" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px;">
</div>
A Python-based application for classifying acne using a YOLO model. The system allows users to upload images or capture them via a webcam, then uses a pre-trained YOLO model to classify acne types. The GUI is built with Tkinter, and the application integrates OpenCV for image processing and Ultralytics YOLO for object detection.

## Features

- **Image Upload**: Upload an image to classify acne.
- **Webcam Support**: Use a webcam to capture an image for classification.
- **YOLO Model**: Utilizes a pre-trained YOLO model for accurate acne classification.
- **Dynamic UI**: Features a Tkinter-based GUI with a background color-changing effect.
- **Real-Time Camera Feed**: Displays live webcam feed until an image is captured.

## Requirements

- Python 3.7+
- Libraries:
  - `tkinter` (usually included with Python)
  - `ultralytics`
  - `opencv-python`
  - `numpy`
  - `Pillow`
- A webcam (for camera functionality)
- Pre-trained YOLO model (`best.pt`) placed in the specified path (e.g., `C:\Users\Lenovo\Desktop\best.pt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahulkumargit1/acne-classification-system.git
   cd acne-classification-system
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install ultralytics opencv-python numpy Pillow
   ```

4. Ensure your webcam is connected (if using camera functionality).

5. Place the pre-trained YOLO model (`best.pt`) in the correct path as specified in the code (`C:\Users\Lenovo\Desktop\best.pt`), or update the path in `acnedetection.py` to match your setup.

## Usage

1. Run the application:

   ```bash
   python acnedetection.py
   ```

2. Use the GUI:

   - **Upload Image**: Click "UPLOAD IMAGE" to select an image from your device.
   - **Use Camera**: Click "USE CAMERA" to start the webcam feed. Click "CAPTURE" to take a photo, then "TURN OFF CAMERA" to stop the feed.
   - **Classify**: After uploading or capturing an image, click "CLASSIFY" to run the YOLO model and view the acne classification result.

## How It Works

- The application uses Tkinter to create a user-friendly GUI.
- Images are processed using OpenCV for capture, resizing, and color conversion.
- The Ultralytics YOLO model (`best.pt`) is used to classify acne types in the provided image.
- Results are displayed in the GUI, indicating the detected acne class (e.g., "THIS IMAGE BELONGS TO: [class_name]").
- The background color of the GUI changes every 5 seconds for a dynamic visual effect.

## Notes

- Ensure the YOLO model file (`best.pt`) is accessible at the path specified in the code. If the path differs on your system, update the `self.model = YOLO(...)` line in `acnedetection.py`.
- If the webcam fails to open, the code attempts to use an alternative index (e.g., `cv2.VideoCapture(1)`). You may need to adjust the index based on your system.
- The application resizes images to 400x300 pixels for display in the GUI.
- For better performance, ensure good lighting when using the webcam.

## Repository Structure

```
acne-classification-system/
├── acnedetection.py    # Main application script
├── README.md           # Project documentation
├── requirements.txt    # Dependencies list
└── .gitignore          # Git ignore file
```

## License

This project is licensed under the MIT License.
