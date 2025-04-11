# 👁 Face Recognition Attendance System 👁

## 📄 Overview

This project is an automated attendance system that uses face recognition to identify individuals from a live video feed and logs their attendance in real-time. Built using Python, OpenCV, and the `face_recognition` library, this system is efficient, easy to use, and includes voice notifications for a more interactive experience.

---

## 🚀 Features

- ✅ **Real-Time Face Detection:** Detects and captures faces using a webcam feed.
- 🧠 **Face Recognition:** Matches detected faces against a pre-stored database of images.
- 🗂️ **Automated Attendance Logging:** Records each recognized individual’s name and timestamp in a CSV file.
---

## 📚 Technology Stack

| Technology        | Purpose                                      |
|------------------|----------------------------------------------|
| Python           | Core programming language                    |
| OpenCV           | Video capturing and image processing         |
| face_recognition | Face detection and recognition library       |
| NumPy            | Image data manipulation                      |
| pyttsx3          | Text-to-speech voice notification            |

---

## 📁 Project Structure

| File/Folder         | Description                                                |
|---------------------|------------------------------------------------------------|
| `Source code.py`    | Main script to run the attendance system                   |
| `image_attendance/` | Folder containing images of registered individuals         |
| `attendance.csv`    | File where attendance records are stored                   |
| `requirements.txt`  | List of required Python libraries                          |
| `README.md`         | Project documentation                                      |

---

## ⚙️ Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Akshint0407/face-recognition-attendance-system.git
   cd face-recognition-attendance-system

2. Install Dependencies Ensure Python 3.6+ is installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. Add Photos of Users

- Place clear, well-lit images of each individual in the image_attendance/ folder.

- Name each image according to the person's name (e.g., elon_musk.jpg).

- You may also refer to test images in the image_attendance/ folder.

4. Run the System

   ```bash
   python main.py

## 🧑‍💻 Usage
- Run Source code.py to start the program.

= Your webcam will activate and begin detecting faces.

- Recognized faces will be logged in attendance.csv with names and timestamps.

- Press ctrl + c to exit the program.

## 🛠️ Troubleshooting
- Face Not Recognized: Ensure images in photos/ are clear, front-facing, and properly named.

- Voice Notification Not Working: Confirm pyttsx3 is installed and your system's TTS engine is supported.

- CSV Not Logging: Check if the file path in main.py is correct and write permissions are allowed.

## 📝 License
- This project is open-source and distributed under the [MIT License](LICENSE.txt).

