Virtual Mouse Using Hand Gestures


🚀 Introduction
The Virtual Mouse Using Hand Gestures is an AI-based project that enables users to control their computer's mouse using hand gestures. This innovative solution leverages computer vision and machine learning techniques to detect and track hand movements, providing an alternative, contactless way to interact with a computer.

🗂️ Project Structure

main.py
The main Python script that contains the core logic for detecting hand gestures and controlling the mouse using OpenCV and util.py.

util.py


A utility module used for calculating the angle and distance of the fingertip using NumPy. This helps in gesture recognition and enhances the modularity of the project.

📦 Features

Real-time hand gesture recognition.
Virtual mouse control (click, drag, and move cursor) using fingertip detection.
Fully functional standalone executable (mouse.exe) for easy usage.
Modular design with utility functions in util.py.


🛠️ Requirements

If you're running the project from source code (main.py and util.py), you'll need the following:

Python 3.x
Required Python Libraries:
OpenCV
Mediapipe
NumPy
PyAutoGUI
You can install the required libraries using:
Copy code
pip install opencv-python mediapipe numpy pyautogui
The mouse.exe file does not require any pre-installed modules and can be run directly on any device with a supported operating system.

🚀 How to Run

Option 1: Run from Source Code
Clone this repository or download the files.
Install the required Python libraries as mentioned above.
Run the main script:
python main.py

⚙️ How It Works

The system captures real-time video feed from your webcam.
Hand Gesture Detection:
Detects the position of the hand and fingertips using MediaPipe.
Calculates the angle and distance of the fingertips using functions in util.py.
Mouse Control:
Maps the hand movement to cursor movement.
Recognizes specific gestures (e.g., pinching for a click, finger spread for drag, etc.) to perform mouse actions.
