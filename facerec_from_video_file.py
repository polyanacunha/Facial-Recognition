# import face_recognition
# import cv2
# import numpy as np

# # Initialize video capture from the first available camera
# video_capture = cv2.VideoCapture(0)

# # Load reference images and learn to recognize them
# polyana_image = face_recognition.load_image_file("Polyana.jpg")
# polyana_face_encoding = face_recognition.face_encodings(polyana_image)[0]

# danrley_image = face_recognition.load_image_file("Danrley.jpg")
# danrley_face_encoding = face_recognition.face_encodings(danrley_image)[0]

# # Create arrays of face encodings and corresponding names
# known_face_encodings = [polyana_face_encoding, danrley_face_encoding]
# known_face_names = ["Polyana", "Danrley"]

# while True:
#     # Capture a single frame of video
#     ret, frame = video_capture.read()

#     # Convert the video from BGR to RGB (for face_recognition)
#     # rgb_frame = frame[:, :, ::-1]
#     rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

#     # Detect face encodings in the current frame
#     face_encodings = face_recognition.face_encodings(rgb_frame)
#     print("Face encodings variable", face_encodings)

#     face_locations = face_recognition.face_locations(rgb_frame)
#     print("Face locations variable", face_locations)

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Check if the face matches any known faces
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

#         name = "Unknown"  # Use "Unknown" if no known face is found

#         # If a match was found in known_face_encodings, use the first one
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw a label with the name below the face
#         cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

#     # Display the result
#     cv2.imshow('Video', frame)

#     # Press 'q' to close the window
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release video capture and close all windows
# video_capture.release()
# cv2.destroyAllWindows()


import face_recognition
import cv2
import numpy as np

# Initialize video capture from the first available camera
video_capture = cv2.VideoCapture(0)

# Load reference images and learn to recognize them
polyana_image = face_recognition.load_image_file("Polyana.jpg")
polyana_face_encoding = face_recognition.face_encodings(polyana_image)[0]

danrley_image = face_recognition.load_image_file("Danrley.jpg")
danrley_face_encoding = face_recognition.face_encodings(danrley_image)[0]

rodrigo_image = face_recognition.load_image_file("rodrigo.jpg")
rodrigo_face_encoding = face_recognition.face_encodings(rodrigo_image)[0]

matheus_image = face_recognition.load_image_file("matheus.jpg")
matheus_face_encoding = face_recognition.face_encodings(matheus_image)[0]

davi_image = face_recognition.load_image_file("davi.jpg")
davi_face_encoding = face_recognition.face_encodings(davi_image)[0]

vinicius_image = face_recognition.load_image_file("vinicius.jpg")
vinicius_face_encoding = face_recognition.face_encodings(vinicius_image)[0]

# Create arrays of face encodings and corresponding names
known_face_encodings = [polyana_face_encoding, danrley_face_encoding, rodrigo_face_encoding, matheus_face_encoding, davi_face_encoding, vinicius_face_encoding]
known_face_names = ["Polyana", "Danrley", "Rodrigo", "Matheus", "Davi", "Vinicius"]

process_this_frame = True

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # rgb_small_frame = small_frame[:, :, ::-1]
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])


        # Detect face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Toggle processing for the next frame
    process_this_frame = not process_this_frame

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Press 'q' to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()