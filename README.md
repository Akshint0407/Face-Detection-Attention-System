Face Recognition Attendance System

📄 Overview

This project is an automated attendance system that uses face recognition to identify individuals from a live video feed and logs their attendance in real time. Built using Python, OpenCV, and face recognition libraries, this system is efficient, easy to use, and features voice notifications for a more interactive experience.

🚀 Features

- Real-Time Face Detection: Detects and captures faces in real-time via a webcam.
- Face Recognition: Matches detected faces against a pre-stored database of images.
- Automated Attendance Logging: Logs each recognized individual’s name and timestamp in a CSV file.
- Voice Notification: Announces the name of each recognized person for instant verification.

 📚 Technology Stack

| Technology       | Purpose                                       |
|------------------|-----------------------------------------------|
| Python       | Core programming language                     |
| OpenCV       | Video capturing and image processing          |
| face_recognition | Face detection and recognition library |
| NumPy        | Array handling and image data manipulation    |
| pyttsx3      | Text-to-speech for voice notifications        |






 📁 Project Structure


| File/Folder           | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `main.py`             | Main script to run the attendance system                      |
| `photos/`             | Directory to store images of registered individuals           |
| `requirements.txt`    | Lists all Python dependencies                                 |
| `README.md`           | Project documentation                                         |
| `attendance_logs/`    | Directory where attendance CSV files are stored               |

---

 ⚙️ Setup and Installation

1.	Clone the Repository:
   ```
   git clone https://github.com/yourusername/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
2.	Install Dependencies: Ensure Python 3.6+ is installed, then run:
pip install -r requirements.txt
3.	Add Photos:
•	Place images of each user in the photos folder.
•	Name each image according to the person’s name, e.g., elon_musk.jpg.
4.	Run the System:
python main.py
 ```
2.Install Dependencies: Ensure Python 3.6+ is installed, then run:
pip install -r requirements.txt
Add Photos of Users:

3.Place clear, well-lit images of each individual in the photos folder.
Name each image according to the person’s name (e.g., elon_musk.jpg).

4.Run the System:
python main.py

**Usage**
1.	Run main.py: Start the program by running main.py.
2.	Camera Activation: The webcam will activate and begin detecting faces.
3.	Automatic Logging: Recognized faces are logged in a CSV file with names and timestamps.
4.	Exit: Press q to stop the program.
**Troubleshooting**
•	Face Not Recognized: Ensure the images in photos/ are clear and properly named.
•	Voice Notification Not Working: Verify pyttsx3 installation and functionality.
•	CSV Not Logging: Confirm correct file path in the code for the CSV file.
**License**
•	This project is open source and distributed under the MIT License.

