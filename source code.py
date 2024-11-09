import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Load images and encode known faces
known_faces = {
    "jobs": face_recognition.face_encodings(face_recognition.load_image_file("photos/jobs.jpg"))[0],
    "ratan tata": face_recognition.face_encodings(face_recognition.load_image_file("photos/tata.jpg"))[0],
    "sadmona": face_recognition.face_encodings(face_recognition.load_image_file("photos/sadmona.jpg"))[0],
    "tesla": face_recognition.face_encodings(face_recognition.load_image_file("photos/tesla.jpg"))[0]
}

# List of people to track for attendance
students = list(known_faces.keys())

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

# Create a CSV file with today's date to store attendance
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file = open(current_date + '.csv', 'w+', newline='')
csv_writer = csv.writer(csv_file)

# Write CSV header
csv_writer.writerow(['Name', 'Time'])

while True:
    # Capture each frame from the webcam
    _, frame = video_capture.read()

    # Resize frame for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (OpenCV uses) to RGB (face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Detect face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Check if the detected face matches any known face encodings
        matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
        name = "Unknown"

        # Calculate the distance between the detected face and known faces, find the closest match
        face_distances = face_recognition.face_distance(list(known_faces.values()), face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = list(known_faces.keys())[best_match_index]

        face_names.append(name)

        # Mark attendance if the person is recognized and in the students list
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H:%M:%S")
            csv_writer.writerow([name, current_time])
            print(f"{name} marked present at {current_time}")

    # Display the video with recognized face names
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected on was scaled down
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image with face recognition and attendance marking
    cv2.imshow("Face Recognition Attendance System", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
csv_file.close()
