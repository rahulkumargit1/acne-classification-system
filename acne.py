import tkinter as tk
from tkinter import filedialog, ttk
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image, ImageTk
import random

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acne Classification System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Load YOLO model
        self.model = YOLO(r'C:\Users\Lenovo\Desktop\best.pt')

        # Header
        header_label = tk.Label(root, text="Acne Classification Model", font=("Arial", 24), bg="#2c3e50", fg="white", padx=10, pady=10)
        header_label.pack(fill=tk.X)

        # Button frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        # Upload Image Button
        self.upload_button = ttk.Button(self.button_frame, text="UPLOAD IMAGE", command=self.upload_image, style="Custom.TButton")
        self.upload_button.grid(row=0, column=0, padx=(10, 0))

        # Use Camera Button
        self.camera_button = ttk.Button(self.button_frame, text="USE CAMERA", command=self.use_camera, style="Custom.TButton")
        self.camera_button.grid(row=0, column=1, padx=(10, 0))

        # Camera Label
        self.camera_label = tk.Label(self.root)
        self.camera_label.pack()

        # Capture Button
        self.capture_button = ttk.Button(self.root, text="CAPTURE", command=self.capture_image, style="Custom.TButton")
        self.turn_off_button = ttk.Button(self.root, text="TURN OFF CAMERA", command=self.turn_off_camera, style="Custom.TButton")

        # Classify Button
        self.classify_button = ttk.Button(self.root, text="CLASSIFY", command=self.classify_image, style="Custom.TButton")

        # Result Label
        self.result_label = tk.Label(self.root, text="THIS IMAGE BELONGS TO:", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        # Start background color change
        self.start_bg_color_change()

        # Variable to hold captured image and camera object
        self.captured_image = None
        self.camera = None

    def upload_image(self):
        """Handles image upload and updates the display."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.captured_image = cv2.imread(file_path)  # Ensure new image is captured
            self.display_image(file_path)  # Display new image
            self.classify_button.pack()

    def use_camera(self):
        """Activates the webcam to capture an image."""
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
        
        if not self.camera.isOpened():
            self.camera = cv2.VideoCapture(1)  # Try another index if 0 fails

        if self.camera.isOpened():
            self.show_camera()
            self.camera_label.pack()
            self.capture_button.pack()
            self.turn_off_button.pack()

    def display_image(self, image_path):
        """Displays an image in the GUI."""
        image = cv2.imread(image_path)
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (400, 300))  # Resize for display
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image)
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo

    def show_camera(self):
        """Continuously updates the camera feed in the GUI."""
        if self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (400, 300))  # Resize for display
                self.captured_image = frame
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                self.camera_label.configure(image=photo)
                self.camera_label.image = photo
            self.root.after(10, self.show_camera)  # Keep updating

    def capture_image(self):
        """Captures an image from the webcam."""
        if self.captured_image is not None:
            cv2.imwrite("captured_image.jpg", cv2.cvtColor(self.captured_image, cv2.COLOR_RGB2BGR))
            self.display_image("captured_image.jpg")
            self.release_camera()  # Properly release the camera
            self.classify_button.pack()

    def classify_image(self):
        """Triggers image classification using the YOLO model."""
        if self.captured_image is not None:
            cv2.imwrite("temp_image.jpg", cv2.cvtColor(self.captured_image, cv2.COLOR_RGB2BGR))  # Save a temporary image
            self.detect_objects("temp_image.jpg")

    def detect_objects(self, image_path):
        """Performs object detection and displays classification results."""
        results = self.model(image_path)
        names_dict = results[0].names
        probs = results[0].probs.data.tolist()

        highest_prob_class = names_dict[np.argmax(probs)]

        # Display the detected object class
        self.result_label.config(text=f"THIS IMAGE BELONGS TO: {highest_prob_class}")

    def turn_off_camera(self):
        """Stops the camera feed and releases resources."""
        self.release_camera()
        self.camera_label.pack_forget()
        self.capture_button.pack_forget()
        self.turn_off_button.pack_forget()

    def release_camera(self):
        """Safely releases the camera if it's open."""
        if self.camera and self.camera.isOpened():
            self.camera.release()
            self.camera = None

    def start_bg_color_change(self):
        """Initiates the background color-changing effect."""
        self.change_bg_color()

    def change_bg_color(self):
        """Changes the background color at regular intervals."""
        r = random.randint(180, 255)
        g = random.randint(180, 255)
        b = random.randint(180, 255)
        new_bg_color = f"#{r:02x}{g:02x}{b:02x}"

        # Change background color
        self.root.configure(bg=new_bg_color)

        # Schedule the next color change after 5 seconds
        self.root.after(5000, self.change_bg_color)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Custom.TButton", background="#f0f0f0", foreground="black", font=("Arial", 12), borderwidth=0)
    app = ObjectDetectionApp(root)
    root.mainloop()
